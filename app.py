from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    besked = data.get("besked", "")
    return jsonify({"svar": f"Du skrev: {besked}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
