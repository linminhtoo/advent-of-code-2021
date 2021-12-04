from collections import defaultdict
from copy import deepcopy

def filter_nums(kept: list, keep_num: int = 0):
    total = len(kept)

    idx = 0  # digit index
    while len(kept) > 1 and idx < len(kept[0]):
        freq = defaultdict(int)  # track freq of 1's for each digit index
        for x in kept:
            for i in range(len(x)):
                freq[i] += (x[i] == "1")

        if freq[idx] >= total - freq[idx]:
            curr_keep = str(keep_num)
        else:
            curr_keep = str(1 - keep_num)

        kept_ = []
        for x in kept:
            if x[idx] == curr_keep:
                kept_.append(x)
        kept = deepcopy(kept_)  # update kept list of numbers
        total = len(kept)
        idx += 1

    return kept

def solve(X: list) -> int:
    kept_1 = filter_nums(X, 1)
    o2 = int(''.join(list(map(str, kept_1))), 2)

    kept_0 = filter_nums(X, 0)
    co2 = int(''.join(list(map(str, kept_0))), 2)
    return o2 * co2

if __name__ == "__main__":
    for fname in ["3a_test.txt", "3a.txt"]:
        with open(fname, "r") as f:
            x = [l.strip() for l in f.readlines()]
        print('#'*10, fname, '#'*10)
        print(solve(x))
        print('#'*30, '\n')