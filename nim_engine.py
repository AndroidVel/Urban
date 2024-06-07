from random import randint

MAX_BUNCHES = 5
MAX_BUNCHES_SIZE = 20

_holder = {}

def put_stones():
    global _holder
    _holder = {}
    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = (randint(1, MAX_BUNCHES_SIZE))


def take_from_bunche(position, quantity):
    if position in _holder:
        _holder[position] -= quantity


def get_bunches():
    return _holder.values()


def is_game_over():
    return sum(_holder.values()) == 0

