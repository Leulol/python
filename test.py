#1 Personal Information Collector

def personal_info_collector():
    print("=== Personal Information Collector ===")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    grade = input("Enter your grade: ")
    hobby = input("Enter your hobby: ")

    print("=== Collected Information ===")
    print(f"Hello, my name is {name}. I'm {age} years old and in Grade {grade}. I love {hobby}.")
    print(f"And I will be {age + 1} years old next year.")

if __name__ == "__main__":
    # This code runs only if the script is executed directly, not if imported
    personal_info_collector()

#2 Lucky Number Game
import random

def lucky_number_game():
    print("=== Lucky Number Game ===")
    lucky_number = random.randint(1, 10)  # Generate a random number between 1 and 10

    while True:
        guess = int(input("Guess my lucky number (between 1 and 10): "))
        if guess == lucky_number:
            print(f"Congratulations! You guessed it right. The number is {guess}")
            break
        elif guess < lucky_number:
            print("The lucky number is higher")
        elif guess > lucky_number:
            print("The lucky number is lower")

# To run only the lucky number game:
if __name__ == "__main__":
    lucky_number_game()

#3 simple chatbot
def chat_bot():
    print("=== Chat Bot ===")
    print("Hello! I'm a chat bot. What is your name?")
    name = input("Enter your name: ")
    print(f"Nice to meet you, {name}! I want to get some information about you.")

    while True:#loop to keep asking questions
        print("How old are you? And where do you learn?")
        age = int(input("Enter your age: "))
        school = input("Enter your school: ")
        print(f"So you are {age} years old and you learn at {school}. Nice!")

        print("What is your favorite subject?")
        subject = input("Enter your favorite subject: ")
        if subject.lower() == "ict":
            print("That's great! ICT is also my favorite subject.")
        else:
            print(f"{subject} is a great subject.")

        more = input("Do you want to answer more questions? (yes/no): ")
        if more.lower() != "yes":
            print("Thank you for chatting! Goodbye!")
            break

if __name__ == "__main__":
    chat_bot()

#5 temperature converter
def temperature_converter():
    print("=== Temperature Converter ===")
    print("Type 'C' to convert from Fahrenheit to Celsius.")
    print("Type 'F' to convert from Celsius to Fahrenheit.")
    print("Type 'K' to convert from Celsius to Kelvin")
    print("Type 'C!' to change from Kelvin to Celsius")
    print("Type 'F!' tp change from Kelvin to Fahrenheit")
    print("Type 'K!' to change from Fahrenheit to Kelvin")
    choice = input("Your choice (C/F/K/C!/F!/K!): ").strip().upper()

    if choice == 'C':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5 / 9
        print(f"{f}°F is {c:.2f}°C")#.2f will format the float number to 2 decimal places
    elif choice == 'F':
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9 / 5) + 32
        print(f"{c}°C is {f:.2f}°F")#.2f will format the float number to 2 decimal places
    elif choice == 'K':
        c = float(input("Enter temperature in Celsius: "))
        k = c + 273
        print(f"{c}°C is {k:.2f}K")
    elif choice == 'C!':
        k = float(input("Enter temperature in Kelvin: "))
        c = k - 273
        print(f"{k}K is {c:.2f} Celsius")
    elif choice == 'F!':
        k = float(input("Enter temperature in Kelvin: "))
        f = 9 / 5 * (k - 273) + 32
        print(f"{k}Kelvin is {f:.2f}Fahrenheit")
    elif choice == 'K!':
        f = float(input("Enter temperature in Fahrenheit: "))
        k = 5 / 9 * (f-32) + 273
        print(f"{f} is {k:.2f}")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    temperature_converter()
#python calculater
def simple_calculater():
    print("which do you want (+)/(-)/(*)/(/)")
    arithmatic = input("(+)/(-)/(*)/(/): ")
    x = int(input("the value of x: "))
    y = int(input("the value of y: "))
    if arithmatic == "+":
        result = x + y
        print(int(result))
    elif arithmatic == "-":
        result = x - y
        print(int(result))
    elif arithmatic == "*":
        result = x * y
        print(int(result))
    elif arithmatic == "/":
        result = x / y
        print(int(result))
    else:
        print("invalid input")
if __name__ == "__main__":
    simple_calculater()
    # circumference
    print("===Circumference===")
    import math


def circumference():
    r = float(input("Enter the radius of the circle: "))
    c = float(2 * math.pi * r)
    print(f"The circumference of the circle is {c:.3f}")


if __name__ == "__main__":
    circumference()
# area
print("===Area===")


def area():
    r = float(input("Enter the radius of the circle: "))
    a = float(math.pi * pow(r, 2))
    print(f"The Area of the circle is {a:.3f}")
if __name__ == "__main__":
    area()
#Username validation
print("===User validation===")
def user():
    username = input("Enter your user name:")
    if len(username) > 12:
        print("your user name is not valid")
    elif username.find(" ") == -1:
        print("There should not be any space in the user name")
    elif not username.isalpha():
        print("there should not be any digit")
    else:
        print(f"Welcome {username}!")
if __name__ == "__main__":
    user()

#count down by sec and min
import time
def timer():
    my_time = int(input("enter the time in secondes: "))
    for x in range(my_time, -1, -1):
        mins = x / 60
        seconds = x % 60
        print(f"00:{mins:.02}:{seconds:02}")
        time.sleep(1)#after each iteration you will sleep for 1 second or pause the program

print("TIMES UP!!")
if __name__ == "__main__":
    timer()
#game
def game():
    import time
    import random

    def slow_print(text, delay=0.04):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def intro():
        slow_print("You wake up in a dark forest...")
        time.sleep(1)
        slow_print("A path splits into two ahead of you.")
        time.sleep(1)
        choice = input("Do you go left or right? ").lower()
        if choice == "left":
            forest_path()
        elif choice == "right":
            cave_path()
        else:
            slow_print("Confused, you stand still until night falls...")
            game_over()

    def forest_path():
        slow_print("You walk down the forest path.")
        time.sleep(1)
        slow_print("A wild beast jumps out!")
        fight("Beast")

    def cave_path():
        slow_print("You enter a dark cave...")
        time.sleep(1)
        slow_print("You find a glowing sword on the ground!")
        inventory.append("Sword")
        time.sleep(1)
        slow_print("Suddenly, a shadowy monster appears!")
        fight("Shadow Monster")

    def fight(enemy):
        slow_print(f"A {enemy} appears!")
        time.sleep(1)
        if "Sword" in inventory:
            slow_print("You use your sword to defeat the monster!")
            win()
        else:
            choice = input("Do you fight with your fists or run? (fight/run): ").lower()
            if choice == "fight":
                result = random.choice(["win", "lose"])
                if result == "win":
                    slow_print(f"You defeat the {enemy} with your bare hands!")
                    win()
                else:
                    slow_print(f"The {enemy} is too strong...")
                    game_over()
            else:
                slow_print("You try to run, but it catches you...")
                game_over()

    def win():
        slow_print("You survived the adventure. You're a hero!")
        time.sleep(1)
        play_again()

    def game_over():
        slow_print("GAME OVER")
        time.sleep(1)
        play_again()

    def play_again():
        again = input("Play again? (yes/no): ").lower()
        if again == "yes":
            inventory.clear()
            intro()
        else:
            slow_print("Thanks for playing!")

    # Inventory to store items
    inventory = []

    # Start the game
    intro()
if __name__ == "__main__":
    game()
#2d loop
def d():
    fruits = ["apple", "banana", "orange"]
    #1d list
    vegetable = ["carrots","potatoes"]
    meat = ["chicken", "fish", "turkey"]
    groceries = [fruits, vegetable, meat]
    print(groceries[0][1])#the list is the row end the element of the list are columns
    for list in groceries:#list is getting every value first(single) of grocery which is now a list, or it becomes fruits
        for elem in list:#list has got the element od groceries(fruits) now elem will get every first(single)/(fruits)
            print(elem)
if __name__ == "__main__":
    d()
#Multiple choice
def choice():
    questions = [
        "What is your name?",
        "How old are you?",
        "What is your favorite food?",
        "Where do you live?"
    ]
    options = [
        ["A. Leul", "B. Mesfin", "C. Abe", "D. Kebe"],
        ["A. 16", "B. 15", "C. 20", "D. 100"],
        ["A. Erteb", "B. Pasta", "C. Shiro", "D. Water"],
        ["A. KK", "B. BB", "C. II", "D. AA"]
    ]
    answers = ["A", "B", "C", "D"]
    user_guesses = []
    score = 0  # Initialize score

    for i in range(len(questions)):
        print(questions[i])
        for opt in options[i]:
            print(opt)
        guess = input("Enter your answer: ").upper()
        user_guesses.append(guess)
        if guess == answers[i]:
            print("✅ You are correct")
            score += 1
        else:
            print(f"❌ The correct answer is {answers[i]}")
        print("-------------------")

    # Show correct answers
    print("\n✅ Correct answers:")
    for ans in answers:
        print(ans, end=" ")
    print()

    # Show user guesses
    print("📝 Your guesses:")
    for guess in user_guesses:
        print(guess, end=" ")
    print()

    # Calculate and show score
    percentage = int(score / len(questions) * 100)
    print(f"\n🎯 Your score: {score} out of {len(questions)}")
    print(f"📊 Percentage: {percentage}%")
if __name__ == "__main__":
    choice()