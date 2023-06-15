from collections import defaultdict


def check(want, number, shopping_basket):
    for i, w in enumerate(want):
        if number[i] > shopping_basket[w]:
            return False
    return True


def solution(want, number, discount):
    answer = 0
    shopping_basket = defaultdict(int)
    for d in discount[:10]:
        shopping_basket[d] += 1
    if check(want, number, shopping_basket):
        answer += 1
    for i, d in enumerate(discount[10:]):
        shopping_basket[d] += 1
        shopping_basket[discount[i]] -= 1
        if check(want, number, shopping_basket):
            answer += 1

    return answer