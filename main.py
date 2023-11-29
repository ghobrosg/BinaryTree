class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self) -> str:
        return str(self.val)


def to_binary_tree(items: list[int]):
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0):
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


def is_symmetric(lst: list) -> bool:
    """
    Given an array, convert it to a binary tree and check if the binary
    tree is symmetric
    >>> is_symmetric([1,2,2,3,4,4,3])
    True
    >>> is_symmetric([1,2,2,None,3,None,3])
    False
    >>> is_symmetric([1,3,3,7,7,7,None])
    False
    >>> is_symmetric([1,3,3,7,7,7,7])
    True
    """
    root = to_binary_tree(lst)

    def dfs(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        x = (left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))
        return x
    return dfs(root.left, root.right)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
