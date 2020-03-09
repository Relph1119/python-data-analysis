import numpy as np

import numpy_exercises.generators as ge


def question(n):
    print(f'{n}. ' + ge.QHA[f'q{n}'])


def hint(n):
    print(ge.QHA[f'h{n}'])


def answer(n):
    print(ge.QHA[f'a{n}'])


def pick():
    n = np.random.randint(1, 100)
    question(n)
    np.set_printoptions()
