import unittest

# TODO: 13....
class TestUnit(unittest.TestCase):
    def test(self):
        self.assertEquals(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]), [2, 4, 1])


def solution(S, P, Q):
    result = [4] * len(P)
    nucle_dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    for i in range(len(P)):
        for j in range(P[i], Q[i]):
            if result[i] > nucle_dict[S[j]]:
                result[i] = nucle_dict[S[j]]
            if S[j] == 'A':
                break
    return result


if __name__ == '__main__':
    unittest.main()
