def solve(actions: list) -> int:
    x, y, aim = 0, 0, 0
    for i in range(len(actions)):
        if actions[i][0] == "forward":
            x += int(actions[i][1])
            y += aim * int(actions[i][1])
        elif actions[i][0] == "down":
            aim += int(actions[i][1])
        elif actions[i][0] == "up":
            aim -= int(actions[i][1])
    return x * y

if __name__ == "__main__":
    for fname in ["2a_test.txt", "2a.txt"]:
        with open(fname, "r") as f:
            x = [l.strip().split(' ') for l in f.readlines()]
        print('#'*10, fname, '#'*10)
        print(solve(x))
        print('#'*30, '\n')