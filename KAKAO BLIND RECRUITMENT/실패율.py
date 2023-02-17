from collections import Counter


def solution(N, stages):
    stages.sort()
    current = 0
    counter = Counter(stages)
    fail = [[0, i + 1] for i in range(N)]
    for i, stage in enumerate(stages):
        if stage != current and stage <= N:
            fail[stage - 1][0] = counter[stage] / len(stages[i:])
            current = stage
    fail.sort(key=lambda x: (-x[0], x[1]))
    return [i[1] for i in fail]