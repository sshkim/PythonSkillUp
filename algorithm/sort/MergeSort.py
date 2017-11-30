import unittest


def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i = j = 0

    while len(left) > i and len(right) > j:
        if left[i] > right[j]:
            result.append(right[j])
            j += 1

        else:
            result.append(left[i])
            i += 1

    result.extend(left[i:] or right[j:])

    return result


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


class TestMergeSort(unittest.TestCase):
    arr = [3, 4, 5, 1, 2, 8, 3, 7, 6]

    def test(self):
        self.assertListEqual(mergeSort(self.arr), [1, 2, 3, 3, 4, 5, 6, 7, 8])
        pass


if __name__ == '__main__':
    unittest.main()
