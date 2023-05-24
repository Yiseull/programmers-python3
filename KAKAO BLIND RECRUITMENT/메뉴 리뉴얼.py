from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        combination = []
        for order in orders:
            combination += combinations(sorted(order), c)
        counter = Counter(combination).most_common()
        answer += [k for k, v in counter if 1 < v == counter[0][1]]

    return [''.join(v) for v in sorted(answer)]