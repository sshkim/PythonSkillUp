import sys

a = list(map(int, input().split()))
b = list(map(int, input().split()))


def compareTriplets(a, b):
    a_score = b_score = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            a_score += 1
        elif a[i] < b[i]:
            b_score += 1

    return a_score, b_score


result_a, result_b = compareTriplets(a, b)

print(result_a, result_b)
