# TODO: Binary Search
import unittest


def binarySearch(arr, num):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2

        if arr[mid] == num:
            return True

        if arr[mid] > num:
            return binarySearch(arr[:mid], num)
        else:
            return binarySearch(arr[mid + 1:], num)


class TestBinarySearch(unittest.TestCase):
    arr = [0, 1, 2, 8, 13, 17, 19, 32, 42, 50]

    def test(self):
        self.assertEqual(True, binarySearch(self.arr, 13))
        self.assertEqual(False, binarySearch(self.arr, 10))


if __name__ == '__main__':
    unittest.main()
