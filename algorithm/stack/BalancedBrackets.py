class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, num):
        self.items.append(num)

    def size(self):
        return len(self.items)


def is_matched(expression):
    if len(expression) % 2 != 0:
        return False

    stack = []
    mid = len(expression) // 2
    for i in range(mid):
        stack.append(expression[i])

    for i in range(mid, len(expression)):
        l_bracket = stack.pop()
        if (l_bracket == '[' and expression[i] == ']') or (l_bracket == '{' and expression[i] == '}') or (l_bracket == '(' and expression[i] == ')'):
            pass
        else:
            return False
    return True


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
