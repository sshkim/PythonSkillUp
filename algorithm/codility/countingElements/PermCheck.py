import unittest


class TestUnit(unittest.TestCase):
    def test(self):
        self.assertEquals(solution([2, 3, 1, 4]), 1)
        self.assertEquals(solution([2, 3, 1, 5]), 0)


def solution(arr):
    arr_list = {}
    for i in range(len(arr)):
        if arr[i] <= 0 or arr[i] > len(arr):
            return 0

        arr_list[arr[i]] = 1

    if len(arr_list.keys()) != len(arr):
        return 0

    return 1


if __name__ == '__main__':
    unittest.main()
