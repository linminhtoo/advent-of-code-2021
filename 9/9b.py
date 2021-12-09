from typing import List
import numpy as np
from collections import deque

def solve(X: List) -> int:
    # pad borders with 9 so we can compare easily in next step
    for i in range(len(X)):
        X[i] = [9] + list(X[i]) + [9]
    X.insert(0, ['9'] * len(X[1]))
    X.append(['9'] * len(X[1]))
    X = np.array(X).astype(int)

    # find the coords of lowest points
    lows = []
    for i in range(1, len(X)-1):  # rmbr to exclude padding
        for j in range(1, len(X[0])-1):
            if X[i][j] < X[i-1][j] and \
                X[i][j] < X[i][j-1] and \
                X[i][j] < X[i+1][j] and \
                X[i][j] < X[i][j+1]:
                lows.append((i, j))

    sizes = []
    for low in lows:
        i, j = low

        # explore all squares until 9 is met, BFS
        size = 1
        dirs = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        q = deque()
        q.append((i, j))  # starting pos
        seen = np.zeros(X.shape).astype(bool)
        seen[i][j] = True

        while q:
            i0, j0 = q.popleft()
            for i in range(4):
                i1 = i0 + dirs[i][0]
                j1 = j0 + dirs[i][1]
                if i1 > 0 and i1 < len(X) and \
                    j1 > 0 and j1 < len(X[0]):
                    if X[i1][j1] != 9 and not seen[i1][j1]:
                        seen[i1][j1] = True
                        q.append((i1, j1))
                        size += 1  # expand the basin
        sizes.append(size)

    sizes = list(reversed(sorted(sizes)))  # descending order
    return sizes[0] * sizes[1] * sizes[2]

if __name__ == "__main__":
    for fname in ["9a_test.txt", "9a.txt"]:
    # for fname in ["9a_test.txt"]:
        with open(fname, "r") as f:
            x = [l.strip() for l in f.readlines()]

        x_ = x
        print(x)
        print('#'*10, fname, '#'*10)
        print(solve(x_))
        print('#'*30, '\n')