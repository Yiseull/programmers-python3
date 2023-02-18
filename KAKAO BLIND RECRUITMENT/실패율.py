from collections import Counter


def solution(N, stages):
    players = len(stages)
    fail = [[0, i + 1] for i in range(N)]
    counter = Counter(stages)
    for i in range(1, N + 1):
        if players:
            clear = counter[i]
            fail[i - 1][0] = clear / players
            players -= clear
    fail.sort(key=lambda x: (-x[0], x[1]))
    return [i[1] for i in fail]