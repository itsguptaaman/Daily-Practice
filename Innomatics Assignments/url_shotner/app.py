import os
from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
import pyshorteners

app = Flask(__name__)

#################################### SQL Alchemy Configuration ############################

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

###########################################################################################

# db = SQLAlchemy(app)


################################## Create a Model ####################################

# @app.before_first_request
# def create_tables():
#     db.create_all()

# class Urls(db.Model):
#     id_ = db.Column("id_", db.Integer, primary_key=True)
#     long = db.Column("long", db.String())
#     short = db.Column("short", db.String(10))

#     def __init__(self, long, short):
#         self.long = long
#         self.short = short


def short_url_fun(long_url):
    try:
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(long_url)
        return short_url
    
    except Exception as e:
        return "Try Again"


@app.route("/", methods=['GET', 'POST'])
def home():
    short_url = []
    long_url = []
    global dt
    if request.method == "POST":
        input_string = request.form.get("input_string")
        long_url.append(input_string)
        short = short_url_fun(input_string)
        short_url.append(short)
        dt = {k:v for (k,v) in zip(long_url, short_url)}
        # obj = Urls(input_string, short)
        # db.session.add(obj)
        # db.session.commit()
    return render_template("home.html", short_url=short_url)

@app.route("/history", methods=['GET', 'POST'])
def history():
    new_dt = dt.copy()
    result = new_dt.items()
    print(result)
    return render_template("history.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)