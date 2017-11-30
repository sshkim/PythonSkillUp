n = int(input())

if 5 < n or n > 50:
    raise ValueError('5 <= n <= 50')

x = list(map(int, input().split(' ')))
w = list(map(int, input().split(' ')))


result = sum(x[i] * w[i] for i in range(n)) / sum(w)

print(result)

