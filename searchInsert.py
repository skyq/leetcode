def test():
    t = [
        {
            'nums': [1, 3, 5, 6],
            'target': 5,
            "index": 2
        },
        {
            'nums': [1, 3, 5, 6],
            'target': 2,
            "index": 1
        },
        {
            'nums': [1, 3, 5, 6],
            'target': 7,
            "index": 4
        },
    ]

    for i in t:
        out = searchInsert(i['nums'], i['target'])
        if out != i['index']:
            raise Exception(f'{i} error: out = {out}')


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i in range(0, len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
            return i

    return i + 1
