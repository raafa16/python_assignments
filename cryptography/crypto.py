alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "XPMGTDHLYONZBWEARKJUFSCIQV"
space = "5"


def main():
    keepGoing = True
    while keepGoing:
        response = menu()
        if response == "1":
            plain = input("text to be encoded: ")
            print(encode(plain))
        elif response == "2":
            coded = input("code to be decyphered: ")
            print(decode(coded))
        elif response == "0":
            print("Thanks for doing secret spy stuff with me.")
            keepGoing = False
        else:
            print("I don't know what you want to do...")


def menu():
    menuTitle = "SECRET DECODER MENU"
    menuOptions = {
        0: 'Quit',
        1: 'Encode',
        2: 'Decode'
    }

    # Show the menu
    print(menuTitle)
    for key in menuOptions.keys():
        print(key, ')', menuOptions[key])

    response = input("What is your choice?: ")

    return response


def encode(plain):
    encodedString = ""

    for char in plain:
        # convert from lowercase to uppercase
        char = char.upper()
        # if the char is a letter present in alpha
        if char in alpha:
            char = char
            # find the index of the letter in alpha
            idx = alpha.index(char)

            # append key to the encoded string
            encodedString += key[idx]
        # if the char is a space, replace with 5
        elif char == ' ':
            encodedString += space

    return encodedString


def decode(coded):
    decodedString = ""

    for char in coded:
        if char in key:
            # find the index of the char in key
            idx = key.index(char)

            # append letter to the decoded string
            decodedString += alpha[idx]
        # if char is a 5, replace with a space
        elif char == '5':
            decodedString += ' '

    return decodedString


if __name__ == "__main__":

    main()
