def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i - 1][0] == phone_book[i][0] and len(phone_book[i - 1]) <= len(phone_book[i]):
            if phone_book[i - 1] == phone_book[i][:len(phone_book[i - 1])]:
                return False

    return True
