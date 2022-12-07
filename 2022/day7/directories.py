"""Find directories with large sizes.

The input is a simulated command session with `cd`, and `ls`
commands. The goal is to sum up the sizes of all directories
with sizes of at most 100,000.

Input comes in on stdin.
"""

import sys

from anytree import Node, PostOrderIter, RenderTree
from anytree.search import find

DIR = "dir"
FILE = "file"


def build_tree(lines):
    """Build the tree from command input as a list of lines."""
    root = Node("", type_=DIR)
    current_dir = root
    in_ls = False
    # skip the first cd into /
    for line in lines[1:]:
        line = line.strip()
        if line.startswith("$ cd"):
            # change the current directory
            in_ls = False
            subdir = line.split(" ", 2)[-1]
            if subdir == "..":
                # Go up a directory
                current_dir = current_dir.parent
            else:
                # Go down a directory
                current_dir = find(
                    current_dir,
                    lambda n: n.name == subdir and n != current_dir,
                    maxlevel=2,
                )
        elif line.startswith("$ ls"):
            # we are going to be in an ls listing now.
            in_ls = True
        else:
            assert in_ls  # only see bare lines when we are in ls
            if line.startswith("dir"):
                # create a subdirectory
                name = line.split(" ", 1)[1]
                Node(name, type_=DIR, parent=current_dir)
            else:
                # create a file with a size
                size, name = line.strip().split(" ", 1)
                size = int(size)
                Node(name, type_=FILE, parent=current_dir, size=size)
    return root


def compute_sizes(tree):
    """Use depth-first iterator to compute sizes for every node."""
    for node in PostOrderIter(tree, filter_=lambda n: n.type_ == DIR):
        node.size = sum(child.size for child in node.children)


def main():
    tree = build_tree(sys.stdin.readlines())
    compute_sizes(tree)
    print(
        sum(
            node.size
            for node in PostOrderIter(tree)
            if node.type_ == DIR and node.size <= 100000
        )
    )


if __name__ == "__main__":
    main()
