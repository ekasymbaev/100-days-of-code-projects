import random
names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
student_scores = {n: random.randint(1, 100) for n in names}

print(student_scores)