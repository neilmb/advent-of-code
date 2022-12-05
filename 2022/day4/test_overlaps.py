
from unittest import TestCase

from overlaps import completely_contains
from overlaps2 import any_overlap

class TestOverlaps(TestCase):

    def test_contains(self):
        self.assertTrue(completely_contains((14, 14), (14, 20)))
        self.assertTrue(completely_contains((14, 20), (14, 14)))

        self.assertFalse(completely_contains((14, 20), (19, 21)))
        self.assertFalse(completely_contains((19, 21), (14, 20)))

    def test_any_overlap(self):
        self.assertTrue(any_overlap((14, 14), (14, 20)))
        self.assertTrue(any_overlap((14, 20), (14, 14)))

        self.assertTrue(any_overlap((14, 20), (19, 21)))
        self.assertTrue(any_overlap((19, 21), (14, 20)))

        self.assertFalse(any_overlap((14,14), (15,15)))
        self.assertFalse(any_overlap((15,15), (14,14)))

