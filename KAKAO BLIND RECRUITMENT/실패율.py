from collections import Counter


def solution(N, stages):
    players = len(stages)
    counter = Counter(stages)
    fail = [[0, i + 1] for i in range(N)]   # [실패율, 스테이지의 번호]
    for i in range(1, N + 1):
        if players: # 현재 스테이지에 도달한 플레이어 수
            clear = counter[i]  # 현재 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
            fail[i - 1][0] = clear / players  # 실패율 계산
            players -= clear
    fail.sort(key=lambda x: (-x[0], x[1]))
    return [i[1] for i in fail]