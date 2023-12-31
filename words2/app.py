from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

WORDS = []
with open("large.txt", 'r') as file:
    for line in file.readlines():
        WORDS.append(line.strip())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("q")
    words = [word for word in WORDS if q and word.startswith(q)]
    return jsonify(words)