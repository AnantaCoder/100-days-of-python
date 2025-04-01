from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 50)
    current_year = datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    # Get age from Agify API
    age_url = f'https://api.agify.io?name={name}'
    age_data = requests.get(url=age_url)
    age_json = age_data.json()
    predicted_age = age_json.get('age', 'unknown')

    # Get gender from Genderize API
    gender_url = f'https://api.genderize.io?name={name}'
    gender_data = requests.get(url=gender_url)
    gender_json = gender_data.json()
    predicted_gender = gender_json.get('gender', 'unknown')

    return render_template('guess.html', name=name, age=predicted_age, gender=predicted_gender)

@app.route('/blog/<num>')
def getblog(num):
    blog_url = 'https://api.npoint.io/b156e28fed2b483aa5cc'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html' , posts = all_posts , num = num)

if __name__ == '__main__':
    app.run(debug=True)
