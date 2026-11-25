#TERO, JOHN CEN O.
#BAET 2101

SECRET = 27
tries = 0

while True:
    guess = int(input("Guess: "))
    tries += 1
    if guess > SECRET:
        print("Too high")
    elif guess < SECRET:
        print("Too low")
    else:
        print(f"Correct! You got it in {tries}'tries.")
        break
