"""
2.zaverecny_ukol.py: druhý projekt do Engeto Online Python Akademie - Bulls and Cows

author: Magdalena Slánská
email: magdalena@slansti.cz
discord: magdalena2586
"""

import random


def hello():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    print("Enter a number:")


def random_number():
    while True:
        # Generate a random permutation of digits 0-9 and select the first 4 digits
        digits = list(range(10))
        random.shuffle(digits)
        random_number = int("".join(map(str, digits[:4])))

        # Ensure the number doesn't start with 0
        if random_number >= 1000:
            return random_number


hello()

# construct 4-digit random number not starting 0
secret = str(random_number())
print(secret)

found = False
while not found:
    user_input = input(">>> ")
    try:
        if len(user_input) != 4:
            raise Exception("Input must be 4 digits")
        if user_input[0] == "0":
            raise Exception("Input must not start with 0")
        
        unique_chars = set()
        for char in user_input:
            if char <= "0" or char >= "9":
                raise Exception("Input must be digits only")
            unique_chars.add(char)
        if len(unique_chars) != 4:
            raise Exception("Input must contain unique digits")
    except Exception as e:
        print(e)