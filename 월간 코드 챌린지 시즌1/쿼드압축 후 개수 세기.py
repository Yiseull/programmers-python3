def solution(arr):
    answer = [0, 0]

    def quad_tree(x, y, n):
        if n == 1:
            return str(arr[x][y])

        half = n // 2
        a = quad_tree(x, y, half)
        b = quad_tree(x + half, y, half)
        c = quad_tree(x, y + half, half)
        d = quad_tree(x + half, y + half, half)

        if (a == '0' or a == '1') and a == b == c == d:
            return a
        else:
            return '(' + a + b + c + d + ')'

    result = quad_tree(0, 0, len(arr))
    answer[0] = result.count('0')
    answer[1] = result.count('1')

    return answer