from bs4 import BeautifulSoup
import requests

url = "https://www.justwatch.com/in/movies"

response = requests.get(url)
website_html = response.text

soup = BeautifulSoup(website_html , 'html.parser')

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("day-45 web scrapping//movies.txt", mode="w") as file:
    for movie in movies:
        print(movie)
        file.write(f"{movie}\n")