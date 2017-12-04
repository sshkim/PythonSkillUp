import unittest


class TestUnit(unittest.TestCase):
    def test(self):
        self.assertEquals(solution([9, 3, 9, 3, 9, 7, 9]), 7)


def solution(arr):
    result_dic = {}
    for i in arr:
        if result_dic.get(i) is None:
            result_dic[i] = 1
        else:
            result_dic[i] += 1

    for k, v in result_dic.items():
        if v % 2 == 1:
            return k

    return -1


if __name__ == '__main__':
    unittest.main()