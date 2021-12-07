from typing import List

def solve(X: List) -> int:
    # smart solution using hashmap, grouping together fishes by their age
    # List was unnecessary to store their positions
    # now, it is O(k) * O(t)
    # where t = number of generations
    # k = number of keys in hashmap, i.e. the range of timers possible, which is just 9 (0 to 8)

    timers = [0] * 9  # number of fishes at each timer
    for x in X:
        timers[x] += 1

    for _ in range(256):
        # shift timer values
        new = timers[0]  # fishes to duplicate
        for i in range(8):
            timers[i] = timers[i+1]
            timers[i+1] = 0
        timers[6] += new
        timers[8] += new

    return sum(timers)

if __name__ == "__main__":
    for fname in ["6a_test.txt", "6a.txt"]:
        with open(fname, "r") as f:
            x = [l.strip() for l in f.readlines()]
            x = list(map(int, x[0].split(',')))

        print(x)
        print('#'*10, fname, '#'*10)
        print(solve(x))
        print('#'*30, '\n')