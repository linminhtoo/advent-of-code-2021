from typing import List

def solve(X: List) -> int:
    start = set(["[", "(", "{", "<"])
    start2end = {
        "[": "]",
        "(": ")",
        "{": "}",
        "<": ">"
    }

    out = []
    for l in X:
        stack = []
        corrupted = False
        for c in l:
            if c in start:
                stack.append(start2end[c])
            else:
                if len(stack) == 0 or stack[-1] != c:
                    corrupted = True
                    break
                else:
                    stack.pop()
        if not corrupted:
            out.append(stack[::-1])

    values = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []
    for l in out:
        score = 0
        for c in l:
            score *= 5
            score += values[c]
        scores.append(score)

    scores = sorted(scores)

    return scores[int(len(scores)//2)]


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