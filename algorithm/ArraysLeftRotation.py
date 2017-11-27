# TODO: Check The Rotation
n, r = map(int, input().split())

a = list(map(int, input().split()))

result = a[r % n: n] + a[0:r % n]

print(*result, sep=' ')
