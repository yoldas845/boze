from flask import Flask, request

app = Flask(__name__)

@app.post("/webhook")
def webhook():
    data = request.get_json() or {}
    print("Gelen mesaj:", data)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=8000)
