from bisect import bisect_left


def solution(citations):
    n = len(citations)
    citations.sort()
    for h in range(citations[-1], -1, -1):
        i = bisect_left(citations, h)
        if n - i >= h:
            return h