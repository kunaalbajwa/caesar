from sys import argv #exit
#print("I know that these are the words the user typed on the command line: ", argv)
from helpers import alphabet_position, rotate_character
def encrypt(text, rot):
#string , integer
    crypto=''
    for char in text:
        crypto=crypto + rotate_character(char, rot)
    return crypto

#print(encrypt("Hello, World!", 5))
def user_input_is_valid(argv):
#make a boolean
    if len(argv)>=2 and argv[1].isdigit():
        return True
    else:
        return False


#print(user_input_is_valid())
