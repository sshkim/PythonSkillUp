def partition(arr, first, last):
    pivot_idx = first

    left_idx = first + 1
    right_idx = last

    done = False

    while not done:

        while left_idx <= right_idx and arr[pivot_idx] >= arr[left_idx]:
            left_idx += 1

        while left_idx <= right_idx and arr[pivot_idx] <= arr[right_idx]:
            right_idx -= 1

        if right_idx < left_idx:
            done = True
        else:
            arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]

    arr[right_idx], arr[first] = arr[first], arr[right_idx]

    return right_idx


def quickSortHelper(arr, first, last):
    if first < last:
        split_idx = partition(arr, first, last)

        quickSortHelper(arr, split_idx + 1, last)
        quickSortHelper(arr, first, split_idx - 1)



def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(arr)
print(arr)
