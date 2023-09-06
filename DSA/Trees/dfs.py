#!/usr/bin/env python3
from collections import deque


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def dfs_traversal_recursive(node: Node):
    """
    TC: O(N)
    worst case: Unbalanced tree, skewed tree - need to traverse all nodes
    best case: Perfectly balanced tree, eg Complete tree - still all nodes needs traversal

    SC: O(N)
    worst ase: unbalnced: max depth of call stack: N
    best case: balanced tree: O(logN)
    """
    result = []
    def _inner_dfs(node) -> None: # think what your recursive fn will return based on that you can decide what will be returned at None Node
        if not node:
            return
        result.append(node.val)
        _inner_dfs(node.left)
        _inner_dfs(node.right)
    
    _inner_dfs(node)
    return result


def dfs_traversal_iterative(node: Node):
    """ Depth First Traversal: PreOrder

    stack only maintains the top level entry
    TC: O(N)
    SC: O(N) -> differs based on height of the tree
    """

    stack = deque()

    stack.append(node)

    dfs_list = []

    while stack:
        node = stack.pop() # removes the right most element TOP element
        dfs_list.append(node.val)

        # right comes fisrt here as we need Root -> Left -> Right
        # with stack the latest element/TOP will be popped; therfore adding right first
        # would put it in the end of the stack and left value keeps getting popped 2, 4, ... then right values
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return dfs_list


# Construct a sample binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(f"Iterative DFS PreOrder: {dfs_traversal_iterative(root)}")
    print(f"Recursive DFS PreOrder: {dfs_traversal_recursive(root)}")

# Iterative DFS PreOrder: [1, 2, 4, 5, 3]
# Recursive DFS PreOrder: [1, 2, 4, 5, 3]