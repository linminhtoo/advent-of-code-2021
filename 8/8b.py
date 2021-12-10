from typing import List
from collections import defaultdict, Counter

def solve(X: List) -> int:
    # segments to be activated to represent each number
    # we order the seven segments clockwise, with top segment as 1, so seven = 123.
    # the middle segment is the last, and counted as the 7th segment
    seg2num = {}
    seg2num['123456'] = 0
    seg2num['23'] = 1
    seg2num['12457'] = 2
    seg2num['12347'] = 3
    seg2num['2367'] = 4
    seg2num['13467'] = 5
    seg2num['134567'] = 6
    seg2num['123'] = 7
    seg2num['1234567'] = 8
    seg2num['123467'] = 9

    all_nums = []
    for pair in X:
        displayed, decode = pair
        len2d = defaultdict(list)  # length of each digit to its string repr
        for d in displayed:
            len2d[len(d)].append(d)

        char2seg = {}  # e.g. string repr character "d" maps to segment 1
        # difference between string repr length 3 (seven) and length 2 (one) --> segment 1
        one_char = list(set(len2d[3][0]) - set(len2d[2][0]))[0]
        char2seg[one_char] = 1

        four = set(len2d[4][0])  # only digit with string repr length 4 is four
        len_fives = len2d[5]  # look at the 3 string reprs with length 5, they represent two, three and five
        five_counts = Counter()
        for repr in len_fives:
            # we count the total number of times each segment of two/three/five gets activated
            five_counts += Counter(repr)

        for k, v in five_counts.items():
            if v == 1:
                if k not in four:
                    # segment 5 is not in four and it only appears once among two, three and five
                    char2seg[k] = 5
                    break

        for repr in len_fives:
            if k in set(repr):
                two = repr  # this string displays 2 when its segments are activated
                break

        for c in two:
            if five_counts[c] == 2:
                # among the 5-segment numbers, the segment that activates twice and is part of two must be segment 2
                char2seg[c] = 2
                break

        four_repr = set(len2d[4][0])
        for t in two:
            # among the segments representing two, the segment that is needed to display four, and has not been used already as segment 2
            # must be segment 7 (the middle segment)
            if t != c and t in four_repr:
                char2seg[t] = 7

        for c in two:
            # the last segment to represent two, that hasn't been used so far, must be segment 4 (the bottom segment)
            if c not in char2seg.keys():
                char2seg[c] = 4

        one_repr = set(len2d[2][0])
        for c in one_repr:
            if c not in char2seg.keys():
                # for the two segments to represent one, the one that hasn't been used (for two), must be segment 3
                char2seg[c] = 3

        eight_repr = set(len2d[7][0])
        for c in eight_repr:
            if c not in char2seg.keys():
                # the only segment we have not used so far is segment 6, which we can find in eight
                char2seg[c] = 6

        curr_rst = []
        for d in decode:  # for each digit in the number to decode
            segs = []
            for c in d:
                segs.append(char2seg[c])  # get all segments to represent digit d
            segs = sorted(segs)  # sort the numbers and join into string
            segs = ''.join(list(map(str, segs)))
            curr_rst.append(seg2num[segs])  # get the number that this set of segments represents

        curr_rst = ''.join(list(map(str, curr_rst)))  # join the 4 digits together into a single integer
        all_nums.append(int(curr_rst))

    return sum(all_nums)

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