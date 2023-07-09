from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Register Student
students = []

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/registrants', methods=['POST', 'GET'])
def registrants():
    return render_template('registered.html', students=students)

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        dorm = request.form.get('dorm')
        if not name or not dorm:
            return render_template('failure.html')
        students.append(f'{name} from {dorm}')
        return redirect('/registrants')
    else:
        return render_template('index.html')

