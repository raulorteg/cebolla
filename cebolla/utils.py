import random
import os
from os.path import dirname, join

def get_username():

    animals_file = join(dirname(__file__), "../data/animals.txt")
    adjectives_file = join(dirname(__file__), "../data/adjectives.txt")

    animal = random.choice(list(open(animals_file))).strip()
    adjective = random.choice(list(open(adjectives_file))).strip()

    return adjective + " " + animal
