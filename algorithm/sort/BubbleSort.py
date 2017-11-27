import unittest


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

    return arr


class TestBubbleSort(unittest.TestCase):
    arr = [5, 3, 11, 23, 50, 1, 28]

    def test(self):
        self.assertListEqual(bubbleSort(self.arr), sorted(self.arr))


if __name__ == '__main__':
    unittest.main()