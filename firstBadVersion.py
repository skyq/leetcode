bad = 0


def test():
    tests = [
        {"n": 2, "bad": 2, "out": 2},
        {"n": 5, "bad": 4, "out": 4},
        {"n": 1, "bad": 1, "out": 1},
        {"n": 100, "bad": 90, "out": 90},
    ]

    for t in tests:
        print('-----------------------')
        global bad
        bad = t['bad']
        out = __run(t['n'])
        if out != t['out']:
            raise Exception(f'{t} error: out = {out}')
    pass


def isBadVersion(version):
    global bad
    return version >= bad


def __run(n):
    if isBadVersion(1):
        return 1

    left = 1
    right = n
    while left < right:
        middle = (left + right) // 2
        print(f'{left} --- {middle} --- {right}')
        if isBadVersion(middle):
            right = middle
        else:
            left = middle + 1
    return left
