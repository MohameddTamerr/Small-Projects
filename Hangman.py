import random

Word_List = ['Apple', 'Banana', 'Human', 'Water', 'House', 'Car', 'Body', 'Sea', 'Sun', 'Head', 'Hand', 'Sun', 'Clock', 'Television', 'Club', 'Powerbank', 'Book', 'Pencil', 'Pen', 'Van', 'Stadium', 'bed', 'Cup', 'Board','distance','dragon','bin', 'crew', 'deck', 'entry', 'year' ,'poem']

def Get_word():
    cp_word = random.choice(Word_List)
    return cp_word

def The_Game(cp_word):
    space = '-' * len(cp_word)
    guess = False
    guess_letters = []
    chances = 6
    answer = input("Are you ready?")
    if answer == 'yes':
        print("Let's go! Good luck!")
    else:
        print("I don't care if you're ready or not. We'll start anyway.")
    print(shape(chances))
    print(space)
    while guess is False and chances > 0:
        player_guess = input("Try to guess the letter or the word:")
        if len(player_guess) == 1:
            if player_guess in guess_letters:
                print("You guessed that letter before.")
            elif player_guess not in cp_word:
                print("That letter is not in the word.")
                chances -= 1
                guess_letters.append(player_guess)
            else:
                print("Right! It is in the word.")
                guess_letters.append(player_guess)
                indices = [i for i, letter in enumerate(cp_word) if letter == player_guess]
                for index in indices:
                    space = space[:index] + player_guess + space[index + 1:]
                print(space)
            print(shape(chances))
        elif player_guess.lower() == cp_word.lower():
            print(f"Congratulations! You guessed the word '{cp_word}'!")
            guess = True
        else:
            print("That is not the correct word.")
            chances -= 1
            print(shape(chances))
        if '-' not in space:
            print("Congratulations! You guessed the word!")
            guess = True
            def shape(chances):
    if chances == 6:
        print("""
        +---+
        |   |
            |
            |
            |
            |
      =========
        """)
    elif chances == 5:
        print("""
        +---+
        |   |
        O   |
            |
            |
            |
      =========
        """)
    elif chances == 4:
        print("""
        +---+
        |   |
        O   |
        |   |
            |
            |
      =========
        """)
    elif chances == 3:
        print("""
        +---+
        |   |
        O   |
       \|   |
            |
            |
      =========
        """)
    elif chances == 2:
        print("""
        +---+
        |   |
        O   |
       \|/  |
            |
            |
      =========
        """)
    elif chances == 1:
        print("""
        +---+
        |   |
        O   |
       \|/  |
        |   |
            |
      =========
        """)
    else:
        print("""
        +---+
        |   |
        O   |
       \|/  |
        |   |
       / \  |
      =========
        """)

cp_word = Get_word().lower()
The_Game(cp_word)
