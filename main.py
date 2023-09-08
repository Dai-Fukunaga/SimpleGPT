from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenAI API key
API_KEY = ""

def query_chatgpt(prompt):
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    body = f'''
    {{
        "model": "gpt-3.5-turbo",
        "messages": [
            {{"role": "user", "content": "{prompt}"}}
        ]
    }}
    '''

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=header, data=body.encode('utf_8'))

    if response.status_code == 200:
        rj = response.json()
        if "choices" in rj and len(rj["choices"]) > 0:
            ans = rj["choices"][0]["message"]["content"]
            return ans
        else:
            return "No response from ChatGPT"
    else:
        return "Error communicating with ChatGPT API"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    prompt = request.form["prompt_text"]
    ans = query_chatgpt(prompt)
    return render_template("answer.html", answer=ans)

if __name__ == "__main__":
    app.run(debug=True)
