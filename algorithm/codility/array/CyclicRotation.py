import unittest


class TestUnit(unittest.TestCase):
    def test(self):
        self.assertEquals(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
        self.assertEquals(solution([1, 2, 3, 4], 4), [1, 2, 3, 4])


def solution(arr, k):
    if len(arr) == 0:
        return arr

    k = k % len(arr)
    return arr[-k:] + arr[:-k]


if __name__ == '__main__':
    unittest.main()
