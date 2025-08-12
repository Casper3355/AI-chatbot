from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Sæt din OpenAI API-nøgle
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_message}]
    )

    return jsonify({"reply": response.choices[0].message["content"]})

@app.route("/", methods=["GET"])
def home():
    return "AI'en kører!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
