def flatten(data):
    l = []
    for i in data:
        if isinstance(i, list):
            l += flatten(i)
        else:
            l.append(i)
    return l

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본", example)
print("변환", flatten(example))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
