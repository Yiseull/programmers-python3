from math import sqrt


def is_prime_number(x):
    if x == '1' or x == '':
        return 0

    x = int(x)
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1


def convert_k_base(n, k):
    base = ''
    while n > 0:
        n, mod = n // k, n % k
        base += str(mod)
    base = base[::-1]
    return base


def solution(n, k):
    base = convert_k_base(n, k)
    answer = 0
    for num in base.split('0'):
        answer += is_prime_number(num)

    return answer