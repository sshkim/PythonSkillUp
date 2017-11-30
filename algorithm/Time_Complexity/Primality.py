p = int(input().strip())


def checkPrimality(num):
    return True


for a0 in range(p):
    n = int(input().strip())
    answer = checkPrimality(n)
    if answer:
        print("Prime")
    else:
        print("Not prime")
