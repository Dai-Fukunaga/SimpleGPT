import requests

# API KEYは外部に公開しないこと
API_KEY = "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"

header = {
    "Content-Type" : "application/json",
    "Authorization" : f"Bearer {API_KEY}",
}

body = '''
{
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "難しかったよー！"}
    ]
}
'''

response = requests.post("https://api.openai.com/v1/chat/completions", headers = header, data = body.encode('utf_8'))

print(response.text)