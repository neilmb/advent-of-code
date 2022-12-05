from unittest import TestCase

from priorities import priority
from priorities2 import find_badge

class TestPriority(TestCase):

    def test_priority(self):
        self.assertEqual(priority("a"), 1)
        self.assertEqual(priority("z"), 26)
        self.assertEqual(priority("A"), 27)
        self.assertEqual(priority("Z"), 52)

    def test_find_badge(self):
        self.assertEqual(find_badge(["a", "a", "a"]), "a")
        with self.assertRaises(AssertionError):
            find_badge(["a", "a", "b"])
        with self.assertRaises(AssertionError):
            find_badge(["ab", "ab", "ab"])
