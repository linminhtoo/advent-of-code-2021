from typing import List
import numpy as np

def solve(X: List) -> int:
    # pad borders with 9 so we can compare easily in next step
    for i in range(len(X)):
        X[i] = [9] + list(X[i]) + [9]
    X.insert(0, ['9'] * len(X[1]))
    X.append(['9'] * len(X[1]))
    X = np.array(X).astype(int)

    # collect heights of lowest points in is_low
    is_low = np.zeros(X.shape)
    for i in range(1, len(X)-1):  # rmbr to exclude padding
        for j in range(1, len(X[0])-1):
            if X[i][j] < X[i-1][j] and \
                X[i][j] < X[i][j-1] and \
                X[i][j] < X[i+1][j] and \
                X[i][j] < X[i][j+1]:
                is_low[i][j] = 1 + X[i][j]

    return int(np.sum(is_low))

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