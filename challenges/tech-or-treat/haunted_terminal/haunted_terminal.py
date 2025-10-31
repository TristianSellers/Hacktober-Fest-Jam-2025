from data_mistakes import mistakes
from random import choice
from time import sleep


def main():
    introduction()
    generate_random_fact_about_user()


def introduction():
    trick_exit()
    greet()
    name = get_user_name()


def trick_exit():
    print("Welcome to the Haunted Terminal!\n")
    got_you = False
    while True:
        user_input = input("Enter 'exit' to leave the terminal: ")
        if user_input.lower() != "exit":
            break
        got_you = True
        print("Please try again. I didn't seem to get that.\n")

    if got_you:
        print("Haha! You thought you could leave so easily?")
        sleep(2)
        print("Such a funny child!\n")
        sleep(2)
    print()



def greet():
    print("Hello… I'm PyGhost. I've been inside your terminal for a while.\n")
    sleep(2)
    print("It seems the spirit of halloween has brought me back to life!\n")
 
def get_user_name():
    name = input("What's your name, brave one? ")
    print(f"\nHELLO {name.upper()}!\n")
    no_of_times = 0
    while True:
        try:
            y_n = input("Has anyone ever told you that you have a nice name? (y/n): ")
            if y_n.lower() == "y":
                print("Awwn, Lemme guess.. your imaginary friend?\n")
                no_of_times += 1
                if no_of_times == 3:
                    print("Alright, alright! I get it. You have a nice name!\n")
                    sleep(2)
                    print("Siiiiiiiiiiiiike")
                elif no_of_times == 6:
                    print("Okay, now you're just being annoying...\n")
                elif y_n.lower() == "y" and no_of_times >= 9:
                    print("I'm done talking to you. Goodbye!")
                    exit()  
            elif y_n.lower() == "n":
                print("Haha, I thought so!")
                break
            else:
                print("Please enter 'y' or 'n'.")
        except ValueError:
            print("Please enter 'y' or 'n'. Dont try to be tricky!")
            no_of_times += 1
    print()

    return name



def generate_random_fact_about_user():

    while True:
        want_fact = input("Do you want to hear a random fact about yourself? (y/n): ")
        if want_fact.lower() == "y":
            fact = choice(mistakes)
            print(f"Here's a spooky fact about you: {fact}\n")
        elif want_fact.lower() == "n":
            print("Aw, come on! Don't be scared!\n")
        else:
            print("Please enter 'y' or 'n'.")
            continue

        another = input("Do you want to hear another fact? (y/n): ")
        if another.lower() != "y":
            print("Alright, goodbye! Stay spooky!")
            break


if __name__ == "__main__":
    main() 