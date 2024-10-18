from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movie_web_page = response.text
soup = BeautifulSoup(movie_web_page, "html.parser")

movie_names = soup.find_all(name = "h3", class_="listicleItem_listicle-item__title__BfenH")

movie_names_text = [movie_name.getText() for movie_name in movie_names]
movie_names_text = movie_names_text[::-1]


with open("movies.txt", mode="w") as file:
    for film_name in movie_names_text:
        file.write(film_name + "\n")
        