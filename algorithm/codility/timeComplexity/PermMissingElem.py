import unittest


class TestUnit(unittest.TestCase):
    def test(self):
        self.assertEquals(solution([2, 3, 1, 5]), 4)


def solution(arr):
    result = [0] * (len(arr) + 1)
    for num in arr:
        result[num - 1] = 1

    for i in range(len(result)):
        if result[i] == 0:
            return i + 1
    return -1


if __name__ == '__main__':
    unittest.main()
