import random 
from art import logo
from art import vs
from game_data import data
from replit import clear
score = 0
something = True
random_number1 = random.randint(0,49)
random_number2= random.randint(0,49)
while something == True:
    random_number1 =random_number2
    random_number2 = random.randint(0,49)
    print(logo)
    print("Contestant A ==> ",data[random_number1]["name"], ",", data[random_number1]["description"],", from ", data[random_number1]["country"] )
    print()
    print(vs)
    print()
    print("Contestant B ==> ",data[random_number2]["name"], ",", data[random_number2]["description"],", from ", data[random_number2]["country"] )

    print(f"Your score = {score}")
    answer= input("Who has more followers on instagram 'A' or 'B' :- ")
    ans = answer.lower()
    if ans =="a":
        if data[random_number1]["follower_count"]< data[random_number2]["follower_count"]:
            clear()
            print(logo)
            print(f"Sorry that was wrong ,Your score was {score} ")
            something = False
        if data[random_number1]["follower_count"] > data[random_number2]["follower_count"]:
            score+=1
            clear()
    if ans =="b":
        if data[random_number1]["follower_count"]> data[random_number2]["follower_count"]:
            clear()
            print(logo)
            print(f"Sorry that was wrong ,Your score was {score} ")
            something = False
        if data[random_number1]["follower_count"] < data[random_number2]["follower_count"]:
            score+=1
            clear()



    

