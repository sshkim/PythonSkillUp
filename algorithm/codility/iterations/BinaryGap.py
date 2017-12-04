import unittest


class TestUnit(unittest.TestCase):
    def test(self):
        self.assertEquals(solution(1041), 5)
        self.assertEquals(solution(15), 0)
        self.assertEquals(solution(20), 1)
        self.assertEquals(solution(9), 2)
        self.assertEquals(solution(529), 4)


def solution(N):
    s = str(bin(N)).strip("0b")

    sl = len(s)
    bg = 0
    temp = 0
    for i in range(sl):

        if s[i] == "0":
            bg += 1
        if s[i] == "1":
            if temp < bg:
                temp = bg
            bg = 0
    return temp


if __name__ == '__main__':
    unittest.main()
