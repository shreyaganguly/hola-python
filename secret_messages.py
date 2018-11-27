import re


def init_game():
    print("Welcome to Secret Messages!!!")
    # TODO: add exceptions, and add infinite loop choice
    choice = input("Please enter if you want to encrypt(e) or decrypt(d) your messages: ")
    if choice != "e" and choice != "d":
        print("Wrong input! Please correct and try again")
        return
    start_messaging(choice)


def start_messaging(choice):
    coding_choice = get_type(choice)
    print("Start {}crypting you message!".format(coding_choice))
    message = input("Enter the message you want to {}crypt: ".format(coding_choice))
    pattern = re.compile('^\w+$')
    if not bool(pattern.match(message)):
        print("Wrong input! Please correct and try again")
        return
    key = input("Enter the numeric key to {}crypt: ".format(coding_choice))
    if not key.isdigit():
        print("Wrong input! Please correct and try again")
        return
    print(code(choice, message, key))


def get_type(choice):
    if choice == "e":
        return "en"
    return "de"


def code(choice, message, key):
    cipher_choice = "ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz0123456789"
    if choice == "e":
        return encode(cipher_choice, message, key)
    return decode(cipher_choice, message, key)


def encode(cipher_choice, message, key):
    encoded_string = ""
    for character in message:
            encoded_character = cipher_choice[(cipher_choice.find(character) + int(key)) % len(cipher_choice)]
            encoded_string += encoded_character
    return encoded_string


def decode(cipher_choice, message, key):
    decoded_string = ""
    for character in message:
        decoded_character_index = (cipher_choice.find(character) - int(key))
        while decoded_character_index < 0:
            decoded_character_index = decoded_character_index + len(cipher_choice)
        decoded_string += cipher_choice[decoded_character_index]
    return decoded_string


init_game()
