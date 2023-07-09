import os
import smtplib
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    dorm = request.form.get('dorm')
    for key in os.environ:
        print(key)
    if not name or not email or not dorm:
        return render_template('failure.html')
    message = "You are Registered!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("kutbuddin.khan22dse@it.sce.edu.in", os.environ("Kkhan@2001"))
    server.sendmail("kutbuddinkhan82@gmail.com", email, message)
    return render_template('success.html')