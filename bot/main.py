from flask import Flask, request
from message_parser import parse
from dosya_gonderen import send_photos

app = Flask(_name_)

@app.post("/webhook")
def webhook():
    veri = request.get_json() or {}

    try:
        metin = veri["entry"][0]["messaging"][0]["message"]["text"]
        gonderen = veri["entry"][0]["messaging"][0]["sender"]["id"]
    except:
        return {"status": "gecersiz"}

    kategori = parse(metin)

    if kategori == "dyson":
        send_photos("dyson")
        return {"status": "ok"}

    return {"status": "tanimsiz"}

if _name_ == "_main_":
    app.run(port=8000)
