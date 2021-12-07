from typing import List
import numpy as np

def solve(X: List) -> int:
    # naive solution, roughly O(2^n) * O(t)
    # t = number of generations, n = initial number of fishes
    # very slow once t > 128

    for _ in range(81):
        for i in range(len(X)):
            X[i] -= 1
            if X[i] < 0:
                X[i] = 6
                X.append(8)
    return len(X)

if __name__ == "__main__":
    for fname in ["6a_test.txt"]:
        with open(fname, "r") as f:
            x = [l.strip() for l in f.readlines()]
            x = list(map(int, x[0].split(',')))

        print(x)
        print('#'*10, fname, '#'*10)
        print(solve(x))
        print('#'*30, '\n')

# Surely, each lanternfish creates a new lanternfish once every 7 days