import random

game = input("What Game 🕹️ do you want to play: ")

if game == "guess":
    def command():
        """Guessing game"""

        top_of_range = input("Type a number: ")

        if top_of_range.isdigit():
            top_of_range = int(top_of_range)

            if top_of_range <= 0:
                print('Please type a number larger than 0 next time.')
                quit()
        else:
            print('Please type a number next time.')
            quit()

        random_number = random.randint(0, top_of_range)
        guesses = 0

        while True:
            guesses += 1
            user_guess = input("Make a guess: ")
            if user_guess.isdigit():
                user_guess = int(user_guess)
            else:
                print('Please type a number next time.')
                continue

            if user_guess == random_number:
                print("You got it!")
                break
            elif user_guess > random_number:
                print("You were above the number!")
            else:
                print("You were below the number!")

        print("You got it in", guesses, "guesses")

elif game == "ttt":
    def command():
        """Rock paper scissors game in terminal"""

        color = {
            "purple" : '\033[95m',
            "cyan" : '\033[96m',
            "darkcyan" : '\033[36m',
            "blue" : '\033[94m',
            "green" : '\033[92m',
            "yellow" : '\033[93m',
            "red" : '\033[91m',
            "end" : '\033[0m',
        }

        user_choice = input("Whats your choice❔ ('r' for rock 'p' for paper and 's' for scissor): ").lower()

        #Computer choice
        computer_choices = ['r','p','s']
        computer = random.choice(computer_choices)
        index = computer_choices.index(computer)

        #Choice name
        choices = ['rock','paper','scissor']
        choice_name = choices[index]

        if user_choice == computer:
            return print('Both the opponent and you chose ✔️  ➖'+ f' {choice_name}({computer})' + ' So it is a tie')   

        if has_won(user_choice, computer):
            return print(color["green"] + "🎊 You won the game of rock-paper-scissor" + color["end"])

        return print(color["red"] + "👎 You lost the game of rock-paper-scissor" + color["end"])

    def has_won(player, opponent):
        if (player == 'r' and opponent == 's') and (player == 's' and opponent == 'p') and (player == 'p' and opponent == 'r'):
            return True

elif game == "dice":
        def command():
            first = random.randint(1,6)
            second = random.randint(1,6)
            print(f'({first}, {second})')
elif game == "guess2":
    def command():
        print("Welcome to my computer quiz!")

        playing = input("Do you want to play? ")

        if playing.lower() != "yes":
            quit()

        print("Okay! Let's play :)")
        score = 0

        answer = input("What does CPU stand for? ")
        if answer.lower() == "central processing unit":
            print('Correct!')
            score += 1
        else:
            print("Incorrect!")

        answer = input("What does GPU stand for? ")
        if answer.lower() == "graphics processing unit":
            print('Correct!')
            score += 1
        else:
            print("Incorrect!")

        answer = input("What does RAM stand for? ")
        if answer.lower() == "random access memory":
            print('Correct!')
            score += 1
        else:
            print("Incorrect!")

        answer = input("What does PSU stand for? ")
        if answer.lower() == "power supply":
            print('Correct!')
            score += 1
        else:
            print("Incorrect!")

        print("You got " + str(score) + " questions correct!")
        print("You got " + str((score / 4) * 100) + "%.")

command()