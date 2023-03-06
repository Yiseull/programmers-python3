def solution(sizes):
    width, length = 0, 0
    for size in sizes:
        if size[0] > size[1]:
            width = max(width, size[0])
            length = max(length, size[1])
        else:
            width = max(width, size[1])
            length = max(length, size[0])

    return width * length