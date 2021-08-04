import random


print("\U0001f608\U0001f608")
print("\U0001f607\U0001f607\U0001f607")
def hangman_game():
    # Initialize 
    words = ["UBUNTU", "PYTHON", "VISHAL", "LOVE", "NODE"]
    word = random.choice(words)
    print(word)
    guess = "-" * len(word)
    wrong_letters = ""

    # Print header
    print("HANGMAN\n")
    print("""
    +-------
    |     
    |    
    |    
    |    
    |
    +---------""")

    # Main game loop
    while True:
        print(f"\U0001f608\U0001f608 Current Guess: {guess} \U0001f608\U0001f608")
        print(f"\U0001f608\U0001f608 Wrong Guesses: {wrong_letters} \U0001f608\U0001f608")
        letter = input("\n \U0001f608\U0001f608 Please enter a letter. => ").upper()

        # Check if the letter is in the word
        if letter in word:
            temp = ""
            for index in range(len(word)):
                if letter == word[index]:
                    temp += letter
                elif guess[index] != "-":
                    temp += guess[index]
                else:
                    temp += "-"
            guess = temp  
        else:
            wrong_letters += letter

        # Check for a winner
        if word == guess:
            print("You win! And you live to play another day!")
            print("""
         O
        \|/
         |
        / \\
    ----------
            """)
            break

        # Print the hangman
        if len(wrong_letters) == 0:
            print("""
    +------
    |     
    |    
    |    
    |    
    |
    +---------""")

        if len(wrong_letters) == 1:
            print("""
    +------+
    |      |
    |      O
    |    
    |    
    |
    +---------""")

        if len(wrong_letters) == 2:
            print("""
    +------+
    |      |
    |      O
    |      |
    |      | 
    |    
    +---------""")

        if len(wrong_letters) == 3:
            print("""
    +------+
    |      |
    |      O
    |     \|/
    |      |
    |    
    +---------""")

        if len(wrong_letters) == 4:
            print("""
    +------+
    |      |
    |      O
    |     \|/
    |      |
    |     / \\
    +---------""")

        if len(wrong_letters) == 5:
            print("""
    +------
    |     |
    |     O
    |    /|\\
    |     |
    |    | |
    +---------""")

        # Check for a loser
        if len(wrong_letters) == 5:
            print("You lose! Sorry sucker!")
            print(f"The word was {word}")
            break
while  True:
    hangman_game()
    user=input("Do you want play again this game: press (Y/N) : ").lower()
    if user=="y":
        continue
    else:
        break


