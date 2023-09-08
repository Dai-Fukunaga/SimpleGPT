import requests
import get_api_key

# APIトークンは外部に公開しないこと
API_KEY = get_api_key.get_api_key()

# チャットGPTに質問する関数
def query_chatgpt(prompt):
    header = {
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {API_KEY}",
    }

    body = '''
    {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content":"''' + prompt + '''"}
        ]
    }
    '''
    response = requests.post("https://api.openai.com/v1/chat/completions", headers = header, data = body.encode('utf_8'))
    rj = response.json()
    return rj["choices"][0]["message"]["content"]

# ここからがメインプログラム
ans = query_chatgpt("Djangoの勉強方法は?")
print(ans)
