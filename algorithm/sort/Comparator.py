n = int(input())

player_dict = {}
for i in range(n):
    name, score = map(input().split(' '))
    player_dict[i] = name


