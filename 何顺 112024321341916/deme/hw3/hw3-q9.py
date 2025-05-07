#此题借助大模型
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum = current_sum * 10 + node.val
            if not node.left and not node.right:  # 叶节点
                return current_sum
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)


# 辅助函数：根据列表构建二叉树（None表示空节点）
def build_tree(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


#e.g
if __name__ == "__main__":
    # 示例1
    root1 = build_tree([1, 2, 3])
    print(Solution().sumNumbers(root1))

    # 示例2
    root2 = build_tree([4, 9, 0, 5, 1])
    print(Solution().sumNumbers(root2))