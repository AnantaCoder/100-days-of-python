from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Flask will look for this in the 'templates/' folder

# To run the app automatically
if __name__ == "__main__":
    app.run(debug=True)
