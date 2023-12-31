import os
import smtplib
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("dorm"):
        return render_template('failure.html')
    file = open("registered.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("name"), request.form.get("dorm")))
    file.close()
    return render_template('success.html')


@app.route('/registrants', methods=['POST', 'GET'])
def registrants():
    with open('registered.csv', 'r') as file:
        reader = csv.reader(file)
        students = list(reader)
    return render_template('registered.html', students=students)
