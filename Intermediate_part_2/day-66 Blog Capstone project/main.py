from flask import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('landing.html')
@app.route("/login", methods = ['POST','GET'])
def login():
    return render_template('login.html')
@app.route("/contact", methods = ['POST','GET'])
def contactme():
    return render_template('contactme.html')


if __name__ == "__main__":
    app.run(debug=True)
    

'''
@app.route("/login", methods = ['POST','GET'])
def login():
user, blogpost , comment = database
register , login , logout , showpost , about , contact , new post  , edit & delete post.
'''