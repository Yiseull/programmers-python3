from collections import defaultdict


def solution(clothes):
    answer = 1

    dict = defaultdict(int)
    for name, kind in clothes:
        dict[kind] += 1

    for value in dict.values():
        answer *= (value + 1)

    return answer - 1