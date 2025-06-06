import random

# List of possible words to guess
word_list = ['python', 'hangman', 'programming', 'developer', 'algorithm', 'computer']

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word with underscores for unguessed letters
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to play the Hangman game
def play_hangman():
    word = choose_word()  # Choose a random word
    guessed_letters = []  # List to store the guessed letters
    incorrect_guesses = 0  # Counter for incorrect guesses
    max_incorrect_guesses = 6  # Set a limit on the number of incorrect guesses

    print("Welcome to Hangman!")
    
    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord to guess: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        # Get the player's guess
        guess = input("Guess a letter: ").lower()
        
        # Check if the input is a valid letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guess is correct
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! '{guess}' is not in the word.")
        
        # Check if the player has guessed the word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        # If the loop ends due to too many incorrect guesses
        print(f"\nGame Over! The word was: {word}")

# Start the game
if __name__ == "__main__":
    play_hangman()
