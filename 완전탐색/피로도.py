def exploration(cnt, k, dungeons) -> None:
    global answer
    answer = max(answer, cnt)

    for i, fatigue in enumerate(dungeons):
        if not visited[i] and k >= fatigue[0]:
            visited[i] = True
            exploration(cnt + 1, k - fatigue[1], dungeons)
            visited[i] = False


def solution(k, dungeons) -> int:
    global answer
    exploration(0, k, dungeons)
    return answer


answer = 0
visited = [False] * 8