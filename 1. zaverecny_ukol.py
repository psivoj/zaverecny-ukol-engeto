"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Magdalena Slánská

email: magdalena@slansti.cz

discord: magdalena2586

"""

username = input("enter username:")
password = input("enter password:")

# seznam credentials (username + password)
users = [
    {"name": "bob", "password": "123"},
    {"name": "ann", "password": "pass123"},
    {"name": "mike", "password": "password123"},
    {"name": "liz", "password": "pass123"}
]
authenticated = False
for user in users:
    if ((user["name"] == username) and (user["password"] == password)):
        authenticated = True
        break

if not authenticated:
    print("unregistered user, terminating the program..")
    quit()

print("Welcome to the app", username)

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

enter_text_number = input("enter text number ")
try:
    text_number = int(enter_text_number)
except:
    print("Input must be integer")
    quit()

if text_number < 1 or text_number > 3:
    print("enter number 1 to 3")
    quit()




text = TEXTS[text_number- 1]
words = text.split()

total_count = len(words)
print("There are", total_count, "words in the selected text.")

title_case_word_count = 0
upper_case_word_count = 0
lower_case_word_count = 0
numbers_count = 0
sum_count = 0

for word in words:
    first_char = word[0]
    if first_char >= "A" and first_char <= "Z":
        title_case_word_count += 1

    word_upper = word.upper()
    if word == word_upper:
        upper_case_word_count += 1

    word_lower = word.lower()
    if word == word_lower:
        lower_case_word_count += 1
        
    try:
        number = int(word)
        numbers_count += 1
        sum_count += number
    except:
        pass



print("There are:", title_case_word_count, "titlecase words in the selected text.")
print("There are:", upper_case_word_count, "uppercase words in the selected text.")
print("There are:", lower_case_word_count, "lowercase words in the selected text.")
print("There are", numbers_count, "numeric strings in the selected text.")
print("The sum of all numbers is", sum_count, "in the selected text.")











        


    

