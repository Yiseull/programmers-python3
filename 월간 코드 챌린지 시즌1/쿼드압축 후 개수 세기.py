def solution(arr):
    answer = [0, 0]

    def quard_tree(x, y, n):
        if n == 1:
            return str(arr[x][y])

        half = n // 2
        a = quard_tree(x, y, half)
        b = quard_tree(x + half, y, half)
        c = quard_tree(x, y + half, half)
        d = quard_tree(x + half, y + half, half)

        if (a == '0' or a == '1') and a == b == c == d:
            return a
        else:
            return '(' + a + b + c + d + ')'

    result = quard_tree(0, 0, len(arr))
    answer[0] = result.count('0')
    answer[1] = result.count('1')

    return answer