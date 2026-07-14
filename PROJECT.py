import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from gigachat import GigaChat
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

import config


#UI
app = FastAPI(title="Travel Помощник")


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

db_url = f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"

engine = create_engine(db_url, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class TravelHistory(Base):
    __tablename__ = "travel_history"
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    ai_text = Column(Text, nullable=False)

Base.metadata.create_all(bind=engine)



client_id = config.CLIENT_ID
auth_key = config.AUTH_KEY

#UI
class WeatherRequest(BaseModel):
    lat: float
    lon: float
    login: str
    password: str


def get_weather_data(lat, lon):
#API(внешний)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
#API client
    response = requests.get(url).json()
    current = response['current_weather']


    return {
        "city": "Санкт-Петербург",
        "temp": round(current["temperature"]),
        "code": current["weathercode"]}

#UI
@app.post("/get-travel-plan")
def make_plan(data: WeatherRequest):
    if data.login != "log" or data.password != "secret":
        return {"ошибка": "Доступ запрещен. Неверный логин или пароль."}
    weather = get_weather_data(data.lat, data.lon)
    prompt = f"Город {weather['city']}, температура {weather['temp']} градусов, код погоды {weather['code']}. Что взять с собой на прогулку и какие 3 места посетить? Отвечай строго по пунктам."

#AI client
    giga = GigaChat(credentials=auth_key, verify_ssl_certs = False)

    ai_response = giga.chat(prompt)

    ai_advice = ai_response.choices[0].message.content

#DB
    db_session = SessionLocal()
    new_log = TravelHistory(
        login=data.login,
        city=weather['city'],
        ai_text=ai_advice)

    db_session.add(new_log)
    db_session.commit()
    db_session.close()

    return {
        "weather_json": weather,
        "ai_recommendation": ai_advice}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("PROJECT:app", host = "127.0.0.1", port = 8000, reload = True)

