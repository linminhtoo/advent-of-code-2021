from typing import List
import numpy as np

def check_victory(b: List[List[int]]) -> bool:
    for i in range(b.shape[0]):
        if np.sum(b[i]) == b.shape[1]:  # check row
            return True
    for j in range(b.shape[1]):
        if np.sum(b, axis=0)[j] == b.shape[0]:  # check col
            return True
    return False

def solve(nums: List, boards: List[List[List[int]]]) -> int:
    boards = np.array(boards)
    called = np.zeros(boards.shape, dtype=bool)

    won = [False] * len(boards)  # track if board at index i has won
    for num in nums:
        for b_i, b in enumerate(boards):
            for i in range(len(b)):
                for j in range(len(b[0])):
                    if b[i][j] == num:
                        called[b_i][i][j] = True
                        if not won[b_i] and check_victory(called[b_i]):
                            won[b_i] = True
                            if sum(won) == len(boards):  # last board to win
                                unmark_sum = np.sum(b * (1 - called[b_i]))
                                return unmark_sum * num

if __name__ == "__main__":
    for fname in ["4a_test.txt", "4a.txt"]:
        with open(fname, "r") as f:
            x = [l.strip() for l in f.readlines()]

        nums = [int(i) for i in x[0].split(',')]

        boards, curr_board = [], []
        for i in range(1, len(x)):
            if x[i] == '':
                if curr_board != []:
                    boards.append(curr_board)
                curr_board = []
            else:
                line = x[i].split(' ')
                line = [int(x) for x in line if x != '']
                curr_board.append(line)
        boards.append(curr_board)

        print('#'*10, fname, '#'*10)
        print(solve(nums, boards))
        print('#'*30, '\n')