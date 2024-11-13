import random
target = random.randint(1, 10000)
guess = None

while guess != target:
    guess = int(input("Guess the number: "))
    if guess > target:
        print("Too high!")
    elif guess < target:
        print("Too low!")
else:
    print("Correct!")