from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([priority, i] for i, priority in enumerate(priorities))
    while 1:
        m = max(q)
        if q[0][0] < m[0]:
            q.append(q.popleft())
            continue
        answer += 1
        if q.popleft()[1] == location:
            break
    return answer