from math import floor
from collections import Counter


def make_multiset(str) -> Counter:
    multiset = Counter()
    tmp = ''

    for s in str:
        if s.isalpha():
            tmp += s.upper()
            if len(tmp) == 2:
                multiset[tmp] += 1
                tmp = tmp[1]
        else:
            tmp = ''

    return multiset


def solution(str1, str2):
    multiset1 = make_multiset(str1)
    multiset2 = make_multiset(str2)

    intersection_len, union_len = 0, 0
    for s in set(multiset1) | set(multiset2):
        intersection_len += min(multiset1[s], multiset2[s])
        union_len += max(multiset1[s], multiset2[s])

    if union_len == 0:
        return 65536

    return floor((intersection_len / union_len) * 65536)