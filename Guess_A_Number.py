import random

def user_input():
    number_of_spaces = 50
    while True:
        entry = input("Insert number between 1 and 100 or [end] to exit the game: ")
        if entry == "end":
            return entry
            break
        elif entry.isnumeric() == False or int(entry) not in range(1,101):
            print(f"{' ' * number_of_spaces}Invalid input. Insert number between 1 and 100 or [end] to exit the game:\n")
        else:
            return int(entry)
            break

computer_choice = random.randint(1,100)

number_of_guesses = 0


while True:
    user_choice = user_input()
    if user_choice == "end":
        break

    number_of_spaces = 59

    number_of_guesses += 1

    if user_choice < computer_choice:
        print(f"{' '* number_of_spaces}Too Low!")
    elif user_choice > computer_choice:
        print(f"{' '* number_of_spaces}Too High!")
    else:
        print()
        print(f"{' '* number_of_spaces}You guessed it in {number_of_guesses} steps, Good Job!\n")
        break