def ransom_note(magazine, ransom):
    if len(ransom) > len(magazine):
        return False

    magazine_dict = {word: 0 for word in magazine}
    for word in magazine:
        magazine_dict[word] += 1

    for word in ransom:
        magazine_dict[word] -= 1

    for v in magazine_dict.values():
        if v < 0:
            return False

    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine[:m], ransom[:n])

if (answer):
    print("Yes")
else:
    print("No")
