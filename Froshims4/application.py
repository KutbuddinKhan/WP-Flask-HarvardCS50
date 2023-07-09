from flask import Flask, render_template, request, redirect
import csv
import codecs

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("dorm"):
        return render_template('failure.html')
    with open("registered.csv", "a", newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow((request.form.get("name"), request.form.get("dorm")))
    return render_template('success.html')


@app.route('/registrants', methods=['POST', 'GET'])
def registrants():
    with codecs.open('registered.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        students = [row for row in reader if row]  # Exclude empty rows
    return render_template('registered.html', students=students)
