def solution(n, left, right):
    arr = []

    for idx in range(left, right + 1):
        i = idx // n + 1
        j = idx % n + 1

        if j <= i:
            arr.append(i)
        else:
            arr.append(j)

    return arr