"""This module handles the communication between GUI and Model."""
import os
import json

from config import JSON_PATH
from model.person import Person


class NameNotGiven(Exception): ...

class AgeNotGiven(Exception): ...


def add(name: str, age: int) -> None:
    """Creates and adds a new Person.
    
    Parameters
    ----------
    name : str
        Name of the Person.
    age : int
        Age of the Person.

    Raises
    ------
    NameNotGiven
        If the name was an empty string.
    AgeNotGiven
        If the age equals 0.
    """
    if name.strip() == "":
        raise NameNotGiven("Name was not given for Person!")
    if age == 0:
        raise AgeNotGiven("Age cannot be 0 for Person!")
    
    Person.objects.append(Person(name, age))
    

def save() -> None:
    """Saves all the Person objects to a json set in config."""
    with open(JSON_PATH, "w") as f:
        json.dump(
            {
                "Persons": [
                    {"Name": p.name, "Age": p.age} for p in Person.objects
                ]
            },
            f,
            indent=4
        )


def read() -> list[Person]:
    """Reads a json set in config and fills up the Person objects.
    
    Returns
    -------
    list[Person]
        The list of the Persons.
    """
    Person.objects = []

    if not os.path.exists(JSON_PATH):
        with open(JSON_PATH, "w") as f:
            json.dump({"Persons": []}, f, indent=4)

    with open(JSON_PATH, "r") as f:
        data = json.load(f)

        for person in data["Persons"]:
            add(person["Name"], person["Age"])

        return Person.objects
