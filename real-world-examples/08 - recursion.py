# Maximum depth of a binary tree
def max_depth(root) -> int:
    def dfs(node) -> int:
        if node is None:
            return 0

        left_depth = dfs(node.left)
        right_depth = dfs(node.right)

        return 1 + max(left_depth, right_depth)

    return dfs(root)