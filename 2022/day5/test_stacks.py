from unittest import TestCase

from stack_moves import _num_stacks, split_stacks, parse_stacks, parse_move, Move, parse_moves, apply_moves


class TestStacks(TestCase):
    def test_num_stacks(self):
        self.assertEqual(_num_stacks(" 1 2 "), 2)
        self.assertEqual(_num_stacks(" 1 2 3 4 5 6 7 8 9"), 9)

    def test_split_stacks(self):
        self.assertEqual(split_stacks("[A] [B]"), ["A", "B"])
        self.assertEqual(split_stacks("    [B]"), ["", "B"])

    def test_split_stacks_error(self):
        self.assertEqual(split_stacks("        [F] [Q]         [Q]        "),
                        ["", "", "F", "Q", "", "", "Q", "", ""])

    def test_parse_stacks(self):
        self.assertEqual(parse_stacks(["[A] [B]", " 1   2 "]), [["A"], ["B"]])
        self.assertEqual(
            parse_stacks(["[A]    ", "[B] [C]", " 1   2 "]), [["A", "B"], ["C"]]
        )

    def test_parse_stacks_error(self):
        self.assertEqual(parse_stacks(["        [F] [Q]         [Q]        ",
                                       " 1   2   3   4   5   6   7   8   9 "]),
                        [[], [], ["F"], ["Q"], [], [], ["Q"], [], []])

    def test_parse_move(self):
        self.assertEqual(parse_move("move 1 from 1 to 2"), Move(1, 1, 2))
        self.assertEqual(parse_move("move 1000 from 19 to 256"), Move(1000, 19, 256))

    def test_parse_moves(self):
        self.assertEqual(
            parse_moves(["move 1 from 1 to 2", "move 1000 from 19 to 256"]),
            [Move(1, 1, 2), Move(1000, 19, 256)],
        )

    def test_apply_moves(self):
        stacks = [["A"], []]
        apply_moves(stacks, [Move(1, 1, 2)])
        self.assertEqual(stacks, [[], ["A"]])

        # check multiples end up in the right order
        stacks = [[], ["A", "B"]]
        apply_moves(stacks, [Move(2, 2, 1)])
        self.assertEqual(stacks, [["B", "A"], []])
