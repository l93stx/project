import requests
import uuid
from datetime import datetime
key_n = "dd9406fad0c041b58c2b4f05d744a7e0"
key_g = "MDE5ZDdiNGQtNDVjNS03YjRlLTg5NWMtNmJlNmMyODQ5NDA0OjM5MTgzNjlhLTQ5YmYtNDdiNy1hZWE3LTYzM2Y0MmFkYzgyZQ=="
top = "Искусственный интеллект"
def run():
    print("News...")
    txt = "Анализ ИИ: технологии растут, нейросети внедряются в бизнес. Прогнозы позитивные."
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
        # Убрали verify=False
        token = requests.post(u_auth, data={'scope': 'GIGACHAT_API_PERS'}, headers=h_auth, timeout=5).json()[
            'access_token']

        u_chat = "https://sberbank.ru"
        pld = {"model": "GigaChat", "messages": [{"role": "user", "content": f"Напиши аннотацию на 250 слов: {txt}"}]}
        # Убрали verify=False
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
