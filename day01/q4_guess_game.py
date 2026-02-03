import random
answer = random.randint(1, 20)
guess = 0
tries = 0
while answer != guess:
    guess = int(input("Input a number :"))
    tries += 1
    if answer > guess:
        print("Too low")
    elif answer < guess:
        print("Too hight")
    else:
        print(f"Correct! tries: {tries}")
    