def solution(prices):
    stack = []
    seconds = [0] * len(prices)

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            index = stack.pop()
            seconds[index] = i - index
        else:
            stack.append(i)

    while stack:
        index = stack.pop()
        seconds[index] = len(prices) - 1 - index

    return seconds