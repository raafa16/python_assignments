alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "XPMGTDHLYONZBWEARKJUFSCIQV"


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


if __name__ == "__main__":

    main()
