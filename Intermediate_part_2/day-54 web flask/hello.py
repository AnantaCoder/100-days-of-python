# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/") #python decorator : additional funcitonality in the python func
def hello():
    return "Hello, World!"







#to run automatically 
if __name__ == "__main__":
    app.run()