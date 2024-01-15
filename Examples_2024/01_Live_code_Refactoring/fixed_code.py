# Python
import sys
from collections import namedtuple
from typing import Dict

UserData = namedtuple("UserData", ["name", "number", "address"])


def load_phonebook() -> Dict[str, UserData]:
    """
    Load the phonebook from the file
    """
    try:
        with open("phonebook.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error loading phonebook")
        sys.exit(1)

    phone_book = {}
    for line in lines:
        user_str = line.split(";")
        if len(user_str) <= 2:
            print(f"Not enough data in phonebook: {line}")
            continue
        user_name = user_str[0]
        number = user_str[1].strip()
        address = user_str[2].strip()
        phone_book[user_name] = UserData(user_name, number, address)

    return phone_book


if __name__ == "__main__":
    phonebook = load_phonebook()

    while True:
        print("Enter a name to look up, or 'q' to quit:")
        name = input()
        if name == "q":
            break
        user = phonebook.get(name)
        if user is None:
            print("Name not found in phonebook")
            continue

        print("The number is: " + user.number)
        print("The address is: " + user.address)
