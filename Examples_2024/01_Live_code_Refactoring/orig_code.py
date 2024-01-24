# Python
import json
import math
import os
import sys
import time

date = "2021-09-30"
version = "1.0.0"
author = "Python Panda"


# Load the phonebook
def load_phonebook():
    try:
        File = open("phonebook.txt", "r")
        lines = File.readlines()
        File.close()  # Dont forget to close the file
    except:
        print("Error loading phonebook")
        sys.exit(1)

    PHONEBOOK = {}
    for line in lines:
        phonestuff = line.split(";")
        if len(phonestuff) > 2:
            name = phonestuff[0]
            n = phonestuff[1].strip()
            a = phonestuff[2].strip()
            PHONEBOOK[name] = (n, a)
        else:
            print("PROBLEM!!!")
    """
    We are building up a nice phoneboooook here.
    Users can look up names and get numbers.
    """

    return PHONEBOOK


# Look up a number in the phonebook
def lookup1(phonebook, name):
    try:
        number = phonebook[name][0]
        return number
    except:
        return "Name not found in phonebook"


# Look up a number in the phonebook
def lookup2(phonebook, name):
    try:
        address = phonebook[name][1]
        return address
    except:
        return "Adress not found in phonebook"


# Main function
def main():
    phonebook = load_phonebook()

    while True:
        print("Enter a name to look up, or 'q' to quit:")
        name = input()
        if name == "q":
            break

        number = lookup1(phonebook, name)
        print("The number is: " + number)

        address = lookup2(phonebook, name)
        print("The address is: " + address)


if __name__ == "__main__":
    main()
