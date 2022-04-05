# from datetime import datetime

from flask import Flask,request
# from flask import request   
app = Flask(__name__)

@app.route("/")
def home():
    datetime = datetime.now()
    return str(datetime)

if __name__ == "__main__":
    app.run(debug=True)





# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()