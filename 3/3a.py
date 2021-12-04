from collections import defaultdict

def solve(X: list) -> int:
    freq = defaultdict(int)
    for x in X:
        for i in range(len(x)):
            freq[i] += (x[i] == "1")

    total = len(X)
    rst = [0] * len(X[0])
    for k, v in freq.items():
        if v > total - v:
            rst[k] = 1

    gamma = int(''.join(list(map(str, rst))), 2)
    rst = [(1 - x) for x in rst]  # flip bits
    eps = int(''.join(list(map(str, rst))), 2)
    return gamma * eps

if __name__ == "__main__":
    for fname in ["3a_test.txt", "3a.txt"]:
        with open(fname, "r") as f:
            x = [l.strip() for l in f.readlines()]
        print('#'*10, fname, '#'*10)
        print(solve(x))
        print('#'*30, '\n')