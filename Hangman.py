from random import choice

# Word bank for the game
word_bank = ['airplane', 'banana', 'dragon', 'ship', 'house', 'robot', 'bird', 'pyramid',
             'suitcase', 'tiger', 'jungle', 'clock', 'table', 'fast', 'tree', 'python']

def choose_word(word_bank):
    """Selects and returns a random word from the word bank."""
    word = choice(word_bank)
    return word

def display_word(word, guessed_letters):
    """Displays the secret word, replacing unguessed letters with underscores (_)
    and revealing already guessed letters."""
    display_str = ""
    for letter in word:
        if letter in guessed_letters:
            display_str = display_str + letter
        else:
            display_str = display_str + "_"
    return display_str

def get_user_guess():
    """Asks the player whether they want to guess a letter or the full word,
    then receives and returns their input."""
    print('1 to guess a letter, 2 to guess the whole word')
    user_choice = int(input('What is your choice? '))
    if user_choice == 1:
        letter = input('Type a letter: ')
        return letter
    else:
        word_guess = input('Type the word: ')
        return word_guess

def set_difficulty():
    """Handles difficulty menu selection (normal, medium, hard)
    and returns the maximum allowed attempts."""
    user_choice = int(input("Type 1 for Normal mode (999 attempts), "
                            "2 for Medium mode (10 attempts), 3 for Hard mode (5 attempts): "))
    if user_choice == 1:
        print('Normal level selected')
        max_errors = 999
        return max_errors
    elif user_choice == 2:
        print('Medium level selected')
        max_errors = 10
        return max_errors 
    else:
        print('Hard level selected')
        max_errors = 5
        return max_errors 

def play():
    """Handles the main Hangman game loop, tracks remaining attempts,
    manages win/loss conditions, and offers to restart."""
    attempts = set_difficulty()
    secret_word = choose_word(word_bank)
    guessed_letters = []

    while "_" in display_word(secret_word, guessed_letters) and attempts > 0:
        print('Current word:', display_word(secret_word, guessed_letters))
        guess = get_user_guess()

        if len(guess) == 1:
            if guess in secret_word:
                print('Well done! The letter is in the word.')
                guessed_letters.append(guess)
                print("You have", attempts, "attempts left!")
            else:
                print("Wrong! The letter is not in the word.")
                attempts = attempts - 1
                print("You have", attempts, "attempts left!")
        else:
            if guess == secret_word:
                print('Well done! You found the secret word!')
                break
            else:
                print("That is not the correct word...")
                attempts = attempts - 1
                print("You have", attempts, "attempts left!")

    if attempts > 0:
        print("You won! The secret word was", secret_word)
    else:
        print("You lost! You have no attempts left.")
        print("The secret word was", secret_word, "!")

    answer = input('Would you like to play again? (yes, no): ')
    if answer == 'yes':
        play()
    else:
        print("Thanks for playing!")

play()