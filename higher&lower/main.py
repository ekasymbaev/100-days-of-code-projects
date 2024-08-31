import random
from data import data
import art
score = 0
a = random.choice(data)
b = random.choice(data)
if a == b:
    b = random.choice(data)



def compare(x: int, y: int) -> str:
    if x > y:
        return "A"
    elif x < y:
        return "B"



game_over = False

while not game_over:
    print(art.logo)
    b = random.choice(data)

    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")

    print(art.vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")

    usr_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    result = compare(a["follower_count"], b["follower_count"])
    if result == usr_choice:
        score += 1
        print(f"You are right! Current score: {score}.")
        if result == "B":
            a = b

    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score {score}")







