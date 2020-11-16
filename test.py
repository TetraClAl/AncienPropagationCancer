from generate_universe import *
from pytest import *
import sqlite3

print("Chocolatines")
print("Cassoulet")


def test_generate_universe():
    assert generate_universe((4, 4)) == [[0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


test_generate_universe()
