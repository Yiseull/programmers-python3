def solution(msg):
    answer = []
    msg = msg.upper()
    dict = {}
    for i in range(65, 91):
        dict[chr(i)] = i - 64

    i = 0
    w = msg[0]
    while 1:
        if i + 1 >= len(msg):  # 마지막 처리되지 않은 글자인 경우
            answer.append(dict[w])
            break

        c = msg[i + 1]
        if w + c in dict:  # 사전에서 현재 입력과 일치하는 가장 긴 문자열 찾기
            w += c

        else:
            answer.append(dict[w])
            dict[w + c] = len(dict) + 1  # w+c에 해당하는 단어를 사전에 등록
            w = c
        i += 1

    return answer