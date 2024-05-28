from random import randint

_holder = []

def put_stones():
    global _holder
    _holder = []
    for i in range(5):
        _holder.append(randint(1, 20))


def take_from_bunche(position, quantity):
    if 1 <= position <= len(_holder):
        _holder[position - 1] -= quantity


def get_bunches():
    return _holder


def is_game_over():
    return sum(_holder) == 0

