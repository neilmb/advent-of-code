"""Find directories with to delete.

The input is a simulated command session with `cd`, and `ls`
commands. The goal is to find the smallest directory to delete
that makes the free space larger than 30,000,000

Input comes in on stdin.
"""

import sys

from anytree import Node, PostOrderIter, RenderTree
from anytree.search import find, findall

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

    current_size = tree.size
    free_space = 70000000 - current_size
    to_delete = 30000000 - free_space

    # find all the dirs with size more than to_delete
    big_enough_dirs = findall(tree, lambda n: n.type_ == DIR and n.size > to_delete)
    print(min(d.size for d in big_enough_dirs))


if __name__ == "__main__":
    main()
