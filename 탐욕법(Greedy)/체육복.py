def solution(n, lost, reserve):
    answer = n - len(lost)

    # 여벌 체육복이 있는 학생이 체육복을 도난당했을 경우
    for i in reserve:
        if i in lost:
            answer += 1
            lost.remove(i)
            reserve.remove(i)

    reserve.sort()
    lost.sort()
    for i in lost:
        for j in reserve:
            if -1 <= i - j <= 1:
                answer += 1
                reserve.remove(j)
                break

    return answer