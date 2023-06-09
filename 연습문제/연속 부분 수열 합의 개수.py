def solution(elements):
    n = len(elements)
    elements.extend(elements)
    answer = set()

    for i in range(1, n + 1):
        for j in range(n):
            answer.add(sum(elements[j:j + i]))

    return len(answer)