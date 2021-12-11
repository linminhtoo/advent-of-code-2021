from typing import List
import numpy as np

def solve(X0: List) -> int:
    l, w = len(X0) + 2, len(X0[0]) + 2
    X = np.ones((l, w)) * -100000
    X[1:l-1, 1:w-1] = np.array(list(map(list, X0))).astype(int)
    X = X.astype(int)

    rst = 0
    T = 100
    for _ in range(T):
        flashed = np.zeros(X.shape).astype(bool)  # which have flashed already
        X += 1

        while True:
            xs, ys = np.where((X > 9) & ~flashed == True)  # which octopous are now flashing
            xs, ys = xs.tolist(), ys.tolist()
            idxs = list(zip(xs, ys))
            flashed[xs, ys] = True

            for x, y in idxs:
                X[x-1, y-1] += 1
                X[x-1, y] += 1
                X[x, y-1] += 1
                X[x+1, y-1] += 1
                X[x-1, y+1] += 1
                X[x+1, y] += 1
                X[x, y+1] += 1
                X[x+1, y+1] += 1

            new_flash = (X > 9) & ~flashed == True
            if np.sum(new_flash) == 0:
                break

        # need to set all flashed to 0
        xs, ys = np.where(flashed == True)
        xs, ys = xs.tolist(), ys.tolist()
        X[xs, ys] = 0

        rst += np.sum(flashed)

    return rst

if __name__ == "__main__":
    for fname in ["11a_test.txt", "11a.txt"]:
    # for fname in ["11a_test.txt"]:
        with open(fname, "r") as f:
            x = [l.strip() for l in f.readlines()]

        x_ = x
        # print(x)
        print('#'*10, fname, '#'*10)
        print(solve(x_))
        print('#'*30, '\n')