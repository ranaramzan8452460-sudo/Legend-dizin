from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>body{text-align:center;font-family:Arial;background:#111;color:white;padding:20px}
    input{padding:12px;width:80%;max-width:300px;border-radius:10px;border:none;margin:10px}
    button{padding:12px 25px;background:gold;border:none;border-radius:10px;font-weight:bold}
    .box{background:#222;margin:10px auto;padding:15px;border-radius:10px;max-width:400px;border-left:4px solid gold}
    </style></head><body>
    <h1>👑 LEGEND DIZIN 👑</h1>
    <p>Stylish Name Maker</p>
    <form action="/name">
    <input name="n" placeholder="Apna Naam Likho..." required>
    <br><button>GENERATE</button>
    </form></body></html>
    '''

@app.route('/name')
def name_page():
    n = request.args.get('n','Legend')
    styles = [f"꧁ {n} ꧂", f"👑 {n} 👑", f"🔥 {n} 🔥", f"⚡ LEGEND {n} ⚡", f"💀 {n} 💀", f"★ {n} ★", f"♛ {n} ♛", f"꧁༒☬{n}☬༒꧂"]
    boxes = "".join([f'<div class="box">{s} <button onclick="navigator.clipboard.writeText(`{s}`)">Copy</button></div>' for s in styles])
    return f'<html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{{text-align:center;font-family:Arial;background:#111;color:white;padding:20px}} .box{{background:#222;margin:10px auto;padding:15px;border-radius:10px;max-width:400px}} button{{margin-left:10px}}</style></head><body><h2>Result for: {n}</h2>{boxes}<br><a href="/" style="color:gold">⬅ Back</a></body></html>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
