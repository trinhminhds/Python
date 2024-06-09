# Project
# Is Unique: Implement an Algorithm to determine if a string has all unique characters.

import unittest as u


def unique(str):
    char_set = {}

    for set in str:
        if set in char_set:
            return False
        char_set[set] = True
    return True


class test(u.TestCase):
    dataT = [("abdc"), ("s325")]
    dataF = [("442"), ("shs")]

    def test_case(self):
        for test in self.dataT:
            actua = unique(test)
            self.assertTrue(actua)

    def test_ca(self):
        for test in self.dataF:
            actua = unique(test)
            self.assertFalse(actua)


if __name__ == "__main__":
    u.main()
