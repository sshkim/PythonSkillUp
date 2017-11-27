def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]


arr = [23, 1, 5, 7, 3, 6, 11]
selectionSort(arr)

for n in arr:
    print('%d' % n, end=' ')
