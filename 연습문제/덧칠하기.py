def solution(n, m, section):
    answer = 0

    cur = 0
    for per in section:
        if cur < per:
            cur = per + m - 1
            answer += 1

    return answer