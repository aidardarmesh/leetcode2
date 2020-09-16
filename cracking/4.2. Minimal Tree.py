class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bst(arr, left, right):
    if left > right:
        return None
    
    if left == right:
        return Node(arr[left])

    mid = left + (right-left) // 2
    node = Node(arr[mid])
    node.left = bst(arr, left, mid-1)
    node.right = bst(arr, mid+1, right)

    return node
