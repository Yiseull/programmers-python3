from collections import Counter


def solution(s):
    answer = []

    s = s.replace('{', '').replace('}', '')
    s = s.split(',')

    for key, value in Counter(s).most_common():
        answer.append(int(key))

    return answer