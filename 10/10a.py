from typing import List

def solve(X: List) -> int:
    start = set(["[", "(", "{", "<"])
    start2end = {
        "[": "]",
        "(": ")",
        "{": "}",
        "<": ">"
    }

    corrupted = []
    for l in X:
        stack = []
        for c in l:
            if c in start:
                stack.append(start2end[c])
            else:
                if len(stack) == 0 or stack[-1] != c:
                    corrupted.append(c)
                    break
                else:
                    stack.pop()

    values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for c in corrupted:
        score += values[c]

    return score


if __name__ == "__main__":
    for fname in ["10a_test.txt", "10a.txt"]:
    # for fname in ["10a_test.txt"]:
        with open(fname, "r") as f:
            x = [l.strip() for l in f.readlines()]

        x_ = x
        # print(x)
        print('#'*10, fname, '#'*10)
        print(solve(x_))
        print('#'*30, '\n')