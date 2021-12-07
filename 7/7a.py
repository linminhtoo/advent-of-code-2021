from typing import List
import numpy as np

def solve(X: List) -> int:
    x_max = max(X)

    # compare and get minimum cost
    min_cost = float("inf")
    for d in range(x_max):
        curr_cost = 0
        for x in X:
            curr_cost += abs(x - d)
        min_cost = min(curr_cost, min_cost)
    return min_cost

if __name__ == "__main__":
    for fname in ["7a_test.txt", "7a.txt"]:
        with open(fname, "r") as f:
            x = [l.strip() for l in f.readlines()]
            x = list(map(int, x[0].split(',')))

        print(x)
        print('#'*10, fname, '#'*10)
        print(solve(x))
        print('#'*30, '\n')