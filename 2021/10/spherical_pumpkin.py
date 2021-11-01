from math import pi
from sympy import Eq, Symbol, solveset

if __name__ == "__main__":
        
    r = Symbol("r")

    surface = 4 * pi * r ** 2
    volume = (4 / 3) * pi * r ** 3

    print(solveset(Eq(surface, volume), r))
