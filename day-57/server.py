from flask import Flask, render_template
from random import randint
import time
import requests
app = Flask(__name__)

@app.route('/')

def home():
    random_num = randint(1, 10)
    current_year = time.localtime().tm_year
    return render_template("index.html", num=random_num, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", person_name=name,  gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)