import random
import art
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
the_num = random.randint(1, 100)
level = 0
dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
if dif == "easy":
    level = 10
elif dif == "hard":
    level = 5
print(art.logo)
while level !=0:
    
    print(f"You have {level} attempts remaining to guess the number.")

    user_num = int(input("Make a guess: "))
    if user_num>the_num:
        print("Too high!")
    elif the_num>user_num:
        print("Too low!")
    else:
        print("You got it! You win!")
        break

    level -= 1
if level == 0:
    print("You are run out of attempts! You lose!")







