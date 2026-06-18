from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == "balaji" and password == "1234":
        return redirect('/dashboard')

    return "Invalid Username or Password"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    return f"Welcome {username}! Registration Successful"

if __name__ == '__main__':
    app.run(debug=True)