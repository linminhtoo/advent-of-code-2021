def solve(x: list) -> int:
    cnt = 0
    for i in range(1, len(x)-2):
        cnt += (x[i+2] > x[i-1])
    return cnt

if __name__ == "__main__":
    for fname in ["1a_test.txt", "1a.txt"]:
        with open(fname, "r") as f:
            x = [int(l.strip()) for l in f.readlines()]
        print('#'*10, fname, '#'*10)
        print(solve(x))
        print('#'*30, '\n')