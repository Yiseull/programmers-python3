def solution(elements):
    n = len(elements)
    answer = set()

    for i in range(n):
        total = elements[i]
        answer.add(total)
        for j in range(i + 1, i + n - 1):
            total += elements[j % n]
            answer.add(total)
    answer.add(sum(elements))

    return len(answer)