import unittest


def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


class TestInsertionSort(unittest.TestCase):
    arr = [2, 5, 7, 3, 54, 32, 1, 23]

    def test(self):
        self.assertListEqual(insertionSort(self.arr), sorted(self.arr))


if __name__ == '__main__':
    unittest.main()
