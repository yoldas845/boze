from flask import Flask, request
from message_parser import parse
from dosya_gonderen import send_photos

app = Flask(_name_)

@app.post("/webhook")
def webhook():
    data = request.get_json() or {}
    
    # Mesaj metnini çek
    try:
        text = data["entry"][0]["messaging"][0]["message"]["text"]
        sender = data["entry"][0]["messaging"][0]["sender"]["id"]
    except:
        return {"status": "invalid payload"}

    category = parse(text)

    if category == "dyson":
        send_photos("dyson")
        return {"status": "ok"}

    return {"status": "unknown message"}

if _name_ == "_main_":
    app.run(port=8000)
