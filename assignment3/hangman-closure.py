# Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        
        display_word = "".join([char if char in guesses else "_" for char in secret_word])
        print(display_word)
        
        return "_" not in display_word

    return hangman_closure

if __name__ == "__main__":
    secret = input("Enter the secret word: ")
    game = make_hangman(secret)
    
    guessed_all = False
    while not guessed_all:
        guess = input("Guess a letter: ")
        guessed_all = game(guess)
        
    print("Congratulations! You guessed the word!")