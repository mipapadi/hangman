import random

while 1:

    # Opening and reading from our word tank.
    with open('words.txt', 'r', encoding='utf-8') as f:
        word = random.choice(f.readlines()).strip()
        print(word)

    #######################################################

    # The heart of hangman's algorithm.
    def hide_word(words):
        hidden = ""
        for letter in words:
            if letter in letters:
                hidden += letter
            else:
                hidden += "-"
        return hidden

    #######################################################

    efforts = 0
    letters = []

    while efforts < 3:
        if 3-efforts >= 2:
            print(f"Remaining lifes: {3-efforts}")
        else:
            print(f"Remaining life: {3-efforts}")

        print(hide_word(word))

        if hide_word(word) == word:
            print("Congratulations! You WIN!")
            break

        given_letter = input("Letter: ")

        while(given_letter.isdigit() == True):
            given_letter = input("Please give only a letter: ")

        if given_letter.upper() in letters:
            print("This letters has already been given.")
        else:
            letters.append(given_letter.upper())
            #print(f"Letters: {letters}")
            if given_letter.upper() not in word:
                print("Does not exist.")
                efforts += 1
                if efforts == 3:
                    print("I am sorry. You lost.")
                    print(f"Word was: {word}")

        if len(given_letter.upper()) > 1:
            if given_letter.upper() == word:
                print("Congratulations! You WIN!")
                break
            else:
                print("I am sorry. You lost.")
                print(f"Word was: {word}")
                break

        print("#"*40)

    #######################################################

    while 1:
        cont = input("Do you want to continue ? (y/n) ")
        if cont == "n":
            print("Thank you for playing.")
            print("Bye!")
            exit()
        elif cont == "y":
            break
        else:
            print("Please give y for yes or n for no.")
