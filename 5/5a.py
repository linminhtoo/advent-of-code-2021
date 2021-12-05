from typing import List
import numpy as np


def solve(x) -> int:
    # build the grid first
    x_max, y_max = 0, 0
    for l in x:
        for pt in l:
            x_max = max(x_max, pt[0])
            y_max = max(y_max, pt[1])

    grid = np.zeros((x_max+1, y_max+1))
    for l in x:
        x0, y0 = l[0]
        x1, y1 = l[1]
        if x0 == x1:  # horizontal
            if y0 > y1:
                grid[x0, y1:y0+1] += 1
            else:
                grid[x0, y0:y1+1] += 1
        elif y0 == y1:  # vertical
            if x0 > x1:
                grid[x1:x0+1, y0] += 1
            else:
                grid[x0:x1+1, y0] += 1

    print(grid.T)
    return np.sum(grid >= 2)

if __name__ == "__main__":
    for fname in ["5a_test.txt", "5a.txt"]:
        with open(fname, "r") as f:
            x = [l.strip() for l in f.readlines()]
            x = [l.split(' -> ') for l in x]
            x_ = []
            for l in x:
                pair = []
                for ll in l:
                    pair.append(list(map(int, ll.split(','))))
                x_.append(pair)

        print('#'*10, fname, '#'*10)
        print(solve(x_))
        print('#'*30, '\n')