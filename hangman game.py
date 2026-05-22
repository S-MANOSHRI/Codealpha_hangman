import random
words = ["python", "apple", "school", "computer", "hangman"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6
display_word = ["_"] * len(word)
hangman_stages = [
    """
     ------
     |    |
          |
          |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    --------
    """
]
print("Welcome to Hangman game!")
while wrong_guesses < max_wrong and "_" in display_word:

    print(hangman_stages[wrong_guesses])
    print("Word:", " ".join(display_word))
    print("Guessed Letters:", " ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter only ONE alphabet letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)
    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong Guess!")
        wrong_guesses += 1
    print("-" * 35)
if "_" not in display_word:
    print("\nCONGRATULATIONS! YOU WON ")
    print("The word was:", word)

else:
    print(hangman_stages[wrong_guesses])
    print("\nGAME OVER")
    print("The word was:", word)