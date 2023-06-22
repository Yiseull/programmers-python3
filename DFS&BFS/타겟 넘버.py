def dfs(i, result, target, numbers):
    if i == len(numbers):
        if result == target:
            global answer
            answer += 1
        return

    dfs(i + 1, result + numbers[i], target, numbers)
    dfs(i + 1, result - numbers[i], target, numbers)


def solution(numbers, target):
    global answer
    dfs(0, 0, target, numbers)
    return answer


answer = 0