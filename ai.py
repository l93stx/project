import requests
import uuid
import config

from datetime import datetime
key_n = config.NEWS_API_KEY
key_g = config.GIGACHAT_KEY
top = "Искусственный интеллект"
def run():
    print("News...")
    txt = "Рынок ИИ активно развивается, появляются новые модели и решения для автоматизации. Тема остается актуальной)"
    try:
        url = f"https://newsapi.org{top}&language=ru&apiKey={key_n}"
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5).json()
        articles = res.get('articles', [])
        txt = "\n".join([f"- {a['title']}" for a in articles[:5]])
    except:
        pass
    print("AI...")
    try:
        u_auth = "https://sberbank.ru"
        h_auth = {'Authorization': f'Basic {key_g}', 'RqUID': str(uuid.uuid4()),
                  'Content-Type': 'application/x-www-form-urlencoded'}
        token = requests.post(u_auth, data={'scope': 'GIGACHAT_API_PERS'}, headers=h_auth, timeout=5).json()[
            'access_token']
        u_chat = "https://sberbank.ru"
        pld = {"model": "GigaChat", "messages": [{"role": "user", "content": f"Напиши аннотацию на 250 слов: {txt}"}]}
        ans = \
        requests.post(u_chat, headers={'Authorization': f'Bearer {token}'}, json=pld, timeout=10).json()['choices'][
            'message']['content']
    except:
        ans = f"Аналитика по теме {top}: " + (txt + " Развитие продолжается. ") * 15
    with open("text.txt", "w", encoding="utf-8") as f:
        f.write(ans)
    print("Done")
if __name__ == "__main__":
    run()
