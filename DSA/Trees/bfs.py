#!/usr/bin/env python3
from collections import deque


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def bfs_traversal_recursive(node: Node):
    """
    Recursive BFS not common approach, use iterative queue approach
    """


def level_order_traversal_iterative(node: Node):
    """Breadth First Search: Left to right level by level order
    
    add: 1
    f,r
    [1]

    add 2, 3
    f    r
    [1,2,3]

    pop the head/first : 1

    [2,3]

    add left and right children of 2,3
    
    TC: O(N) N is the number of nodes in the tree
    SC: O(N) N is the nodes, worst case happens in a balances binary tree as at any point the queue qill
    hold all nodes in the lowest level, best case is O(1) -skewed tree [Not clear needs more investigation]
    """    
    queue = deque()

    queue.append(node)
    level_list = []
    while queue:
        # dequeue ~ remove the first element from queue
        node = queue.popleft()
        level_list.append(node.val)

        # if there is left adn right node only then add else it will fail
        # changing the order by appending right then left will give right to left order 1,3,2,5,4
        # current implementation gives 1,2,3,4,5
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return level_list


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
    print(level_order_traversal_iterative(root))