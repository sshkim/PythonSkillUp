import unittest


def anagrams(a, b):
    offset = ord('a')
    chars = [0] * 26
    for char in a:
        chars[ord(char) - offset] += 1

    for char in b:
        chars[ord(char) - offset] -= 1

    return sum(abs(value) for value in chars)


class TestAnagrams(unittest.TestCase):
    # a = list(map(str, input().split()))
    # b = list(map(str, input().split()))
    a = ['c', 'd', 'e']
    b = ['a', 'b', 'c']

    def test(self):
        self.assertEqual(4, anagrams(self.a, self.b))


if __name__ == '__main__':
    unittest.main()
