from flask import Flask

app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello, {name.capitalize()}! Welcome to the Flask app!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
