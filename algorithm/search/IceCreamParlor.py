# def icecream(flavors, M):
#     flavor_map = {}
#     for idx, flavor in enumerate(flavors):
#         residual = (M - flavor)
#         if residual in flavor_map:
#             # print([flavor_map[residual], idx])
#             # print(sorted([flavor_map[residual], idx]))
#             return sorted([flavor_map[residual], idx])
#         if not flavor in flavor_map:
#             flavor_map[flavor] = idx
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         m = int(input())
#         n = int(input())
#         flavors = map(int, input().split())
#         result_arr = icecream(flavors, m)
#         print(result_arr[0] + 1, result_arr[1] + 1)