from unittest import TestCase

from anytree import Node

from directories import DIR, FILE, build_tree, compute_sizes


class TestDirectories(TestCase):
    def test_compute_sizes(self):
        tree = Node(
            "/",
            type_=DIR,
            children=[
                Node("subdir", type_=DIR, children=[Node("a", type_=FILE, size=100)])
            ],
        )
        compute_sizes(tree)
        self.assertEqual(tree.size, 100)

    def test_build_tree(self):
        lines = [
            "$ cd /",
            "$ ls",
            "1 file",
            "dir subdir",
        ]
        root = build_tree(lines)
        self.assertEqual(len(root.children), 2)
