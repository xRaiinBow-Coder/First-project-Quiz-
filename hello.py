import random
import os


print("welcome to this quiz, do you have an account:")
account = input("Yes or No?:")

attempts = 3

if account == "No":
    username = input("what is your username?:")
    password = input("what is your password?:")
    password1 = input("please enter your password again for validation: ")
    if password == password1:
        file = open("hello.txt", "w")
        file.writelines(username + ":" + password)
        file.close()
        account = "Yes"

if account == "Yes":
    while attempts > 0:

        LoginUsername = input("username: ")
        LoginPassword = input("what is your password: ")
        file = open("hello.txt", "r")
        data = file.readline()
        file.close()
        if data == LoginUsername + ":" + LoginPassword:
            print("welcome to the quiz!" + "\n")
            break
        else:
            print("please enter valid details")
            attempts -= 1
            print("Attempts  left", attempts)
        if attempts == 0:
            print("you no longer have any attempts left")
            exit()


score = 0
guessing = 3

print("round one of questions...")
answer = input("are you ready, Y/N?:")

if answer == "Y":
    print("lets get this quiz started." + "\n")
elif answer == "N":
    print("go home")


print("get ready for round one" + "\n")
questions = [
    ["Where is Sir Ian McKellen from?:", "England"],
    ["who is the wost president ever?:", "Donald Trump"],
    ["when was the second millennium?:", "year 2000"],
    ["what country has the highest life expectancy?:", "hong kong"],
    ["what is the most common surname in the states?:", "smith"],
    ["who was the ancient greek god of the sun?:", "apollo"]
]
random.shuffle(questions)

for i in range(0, len(questions)):
    print(questions[i][0])
    answer = input("Answer: ")
    if questions[i][1].lower() == answer.lower():
        print(f"correct!" + "\n")
        score += 5
        os.system("cls")
    else:
        score -= 0.5
        guessing -= 1
        print(f"wrong {score}" + "\n")
        print("guesses left", guessing)
    if guessing == 0:
        print("good try")
        exit()

print(f"congrats on round one, your score is...{score} out of 30!")

print("Round 2,this round is on history!, are you ready?: " + "\n")
answer = input("Yes or No:?")

if answer == "Yes":
    print("lets go!")
elif answer == "No":
    print("Bye")
    exit()



questions2 = [
    ["How many wives did henry the 8th have?:", "6"],
    ["what language was spoken in ancient rome?:", "Latin"],
    ["how many years did queen victoria reign", "63 years"],
    ["which president of the USA abolished slavery?:", "Abraham Lincoln"],
    ["what was the final battle of the Napoleonic wars", "Battle of Waterloo"],
    ["which country was ruled by shoguns from 1185 to 1868?:", "japan"],
]

random.shuffle(questions2)

for i in range(0, len(questions2)):
    print(questions2[i][0])
    answer = input("Answer: ")
    if questions2[i][1].lower() == answer.lower():
        print("Correct!" + "\n")
        score += 5
    else:
        score -= 0.5
        guessing -= 1
        print(f"wrong" + "\n")
        print("guesses left", guessing)
    if guessing == 0:
        print("good try")
        exit()

print(f"congrats on round two, your score is...{score} out of 60!" + "\n")

print("Round 3... Finale this rounds theme is pop culture, Do you want to continue?:")
answer = input("Yes or No?:")

if answer == "yes":
    print("welcome to round 3." + "\n")
elif answer == "No":
    print("Bye")
    exit()

questions3 = [
    ["Which popular TV show, inspired by Archie's comics, aired its series finale in 2023?", "Riverdale"],
    ["Which apocalyptic TV drama series was launched by HBO in 2023 based on a popular video game?", "The last of us"],
    [" What is the name of the popular social media app that allows users to create short videos", "Tiktok"],
    [" How many James Bond movies have been made?", "27"],
    ["When was the first Harry Potter book published?", "1997"],
    ["Which Disney movie features a talking snowman named Olaf?", "Frozen"]
]

random.shuffle(questions3)

for i in range(0, len(questions3)):
    print(questions3[i][0])
    answer = input("Answer: ")
    if questions3[i][1].lower() == answer.lower():
        print("Correct!:" + "\n")
        score += 5
    else:
        score -= 0.5
        guessing -= 1
        print("wrong" + "\n")
        print("guesses left", guessing)
    if guessing == 0:
        print("good try")
        exit()

print(f"congrats on round three, your score is....{score} out of 90...wait whats that? a risk it all question?")
answer = input("do you accept.. if you accept and lose, you lose everything...so do you?, Yes or No?.")

if answer == "Yes":
    print("welcome to the final question")
elif answer == "No":
    print(f"thank you for playing, you score is {score} out of 90")

finalQuestion = [
    ["DO YOU SLAY", "yes?"]
]

for i in range(0, len(finalQuestion)):
    print(finalQuestion[i][0])
    answer = input("Answer: ")
    if finalQuestion[i][1].lower() == answer.lower():
        print("Correct:" + "\n")
        score += 100000000000000000
    else:
        score -= 100000000000000000000000000000000000000000000
        guessing -= 1
        print("wrong" + "\n")
        print("guesses left", guessing)
    if guessing == 0:
        print("good try")
        exit()

if finalQuestion == "Correct":
    print(f"YOU'RE A WINNER, YOUR SCORE IS {score}. THANKS FOR PLAYING")
else:
    print(f"good try, your score is {score}")

