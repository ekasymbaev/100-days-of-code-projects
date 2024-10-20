from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
header  = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL, headers=header)

# Check if the request was successful

soup = BeautifulSoup(response.text, "html.parser")

# Find all h3 tags with the specific class that contains the song title
song_names_spans = soup.select("li ul li h3")

# Extract the text and clean up the whitespace
song_names_text = [song.getText().strip() for song in song_names_spans]


with open(f"Best_playlist{date}.txt", "w") as file:
    j = 0
    for i in range(1, 101):
        file.write(f"{i}.{song_names_text[j]}\n")
        j+=1

