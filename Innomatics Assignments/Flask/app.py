from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def home_page():
    return "This is the home page visit /upper route. example:- http://127.0.0.1:5000/upper?name=Aman"


@app.route("/upper")
def to_upper():
    name = request.args.get("name")
    result = name.upper()
    return "Hello " + result + " How are you doing???"


@app.route("/length")
def give_len():
    name = request.args.get("name")
    return "The number of letters in your name is " + str(len(name))


if __name__ == "__main__":
    app.run(debug=True)
