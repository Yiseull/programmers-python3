def solution(n, m, section):
    answer = 0

    cur = 0
    for per in section:
        if cur <= per:
            cur = per + m
            answer += 1

    return answer