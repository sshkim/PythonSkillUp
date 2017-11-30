s = int(input().strip())

"""
111
112
113

121
122
123

131
132
133

211
212
213

"""


def waysWalkUpToStaircase(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0

    result = 0
    for i in range(1, 4):
        if n - i < 0:
            return result
        result += waysWalkUpToStaircase(n - i)
    return result


for a0 in range(s):
    n = int(input().strip())
    print(waysWalkUpToStaircase(n))
