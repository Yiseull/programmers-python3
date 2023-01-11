from collections import Counter


def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    for key, val in participant.items():
        if val != completion[key]:
            return key
    return None