from typing import List

def solve(X: List) -> int:
    x_max = max(X)

    # precompute the cost needed for i steps
    cost_dict = {0: 0}
    curr_cost = 0
    for i, _ in enumerate(range(x_max), start=1):
        curr_cost += i
        cost_dict[i] = curr_cost

    # compare & get minimum cost
    min_cost = float("inf")
    for d in range(x_max):
        curr_cost = 0
        for x in X:
            curr_cost += cost_dict[abs(d - x)]
        min_cost = min(curr_cost, min_cost)
    return min_cost

if __name__ == "__main__":
    for fname in ["7a_test.txt", "7a.txt"]:
        with open(fname, "r") as f:
            x = [l.strip() for l in f.readlines()]
            x = list(map(int, x[0].split(',')))

        print(x)
        print('#'*10, fname, '#'*10)
        print(solve(x))
        print('#'*30, '\n')