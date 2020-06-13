import random

print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']
chosen_word = list(random.choice(words))
solved_word = list("-" * len(chosen_word))
guessed_letters = []
tries = 0

def reset():
    global chosen_word
    global solved_word
    global guessed_letters
    global tries
    chosen_word = list(random.choice(words))
    solved_word = list("-" * len(chosen_word))
    guessed_letters = []
    tries = 0

def menu(choice):
    if choice == "exit":
        exit()
    elif choice == "play":
        game()
    else:
        menu(input('Type "play" to play the game, "exit" to quit: '))

def game():
    global tries
    global words
    global solved_word
    global guessed_letters
    global chosen_word
    while tries < 8:
        if solved_word == chosen_word:
            print("You guessed the word " + "".join(solved_word) + "!")
            print("You survived!")
            reset()
            menu(input('Type "play" to play the game, "exit" to quit: '))
        print("")
        print("".join(solved_word))
        guess = input("Input a letter: ")
        if len(guess) == 1:
            if guess.isalpha():
                if guess.islower():
                     if guess in guessed_letters:
                         print("You already typed this letter")
                     else:
                        guessed_letters.append(guess)
                        if guess in chosen_word:
                            for letter in range(len(chosen_word)):
                                if chosen_word[letter] == guess:
                                    solved_word[letter] = guess
                        else:
                            print("No such letter in the word")
                            tries += 1
                else:
                    print("It is not an ASCII lowercase letter")
            else:
                print("It is not an ASCII lowercase letter")
        else:
            print("You should input a single letter")
    else:
        print("You are hanged!")
        print("")
        reset()
        menu(input('Type "play" to play the game, "exit" to quit: '))

menu(input('Type "play" to play the game, "exit" to quit: '))
