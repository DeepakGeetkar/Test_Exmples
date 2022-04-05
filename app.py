# from pickle import TRUE
from tkinter.tix import COLUMN
from flask import Flask ,render_template,request
from flask_sqlalchemy import SQLAlchemy


from datetime import datetime


app = Flask(__name__)
app.config['SQLALchemy_DATABASE_URI']="mysql://root:@localhost/deepak"
db =SQLAlchemy(app)


class Info(db.model):
    id = db.column(db.Integer,primary_key=True)
    username = db.column(db.String(80),primary_key=True,nullable=False)
    email = db.column(db.String(120),primary_key=True,nullable=False)

@app.route("/")
def hello_world():
    return render_template('index.html')
    # return "<p>Hello, World!</p>"

@app.route("/produts")
def reverse():
    # str = "deepak"
    str = request.args.get('str')
    return str[::-1]

# its a current time and date
@app.route("/currenttime")
def date_time():
    date_time = datetime.now()
    return date_time.strftime("%d/%m/%y    %I:%M:%S")


@app.route('/data')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')


if __name__=="__main__":
    app.run(debug=True ,port=8000)