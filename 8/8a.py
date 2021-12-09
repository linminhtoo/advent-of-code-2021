from typing import List

def solve(X: List) -> int:
    cnt = 0
    for pair in X:
        _, decode = pair
        for num in decode:
            if len(num) in [2, 3, 4, 7]:
                cnt += 1
    return cnt

if __name__ == "__main__":
    for fname in ["8a_test.txt", "8a.txt"]:
        with open(fname, "r") as f:
            x = [l.strip() for l in f.readlines()]
            x = [l.split('|') for l in x]

        x_ = []
        for pair in x:
            curr_pair = []
            for i in pair:
                curr_pair.append(i.strip().split(' '))
            x_.append(curr_pair)

        print('#'*10, fname, '#'*10)
        print(solve(x_))
        print('#'*30, '\n')