from flask import Flask, render_template, request

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

    # words = []
    #q = request.args.get('q')
    # for word in WORDS:
    #     if word.startswith(q):
    #         words.append(word)

    results= [word for word in WORDS if word.startswith(request.args.get('q'))]
    return render_template("search.html", results=results)