#此题借助大模型
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left: TreeNode, right: TreeNode) -> bool:
        # 终止条件
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        # 递归比较：左子树的左 vs 右子树的右，左子树的右 vs 右子树的左
        return self.compare(left.left, right.right) and self.compare(left.right, right.left)


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
    # 示例1：对称树
    root1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    print(Solution().isSymmetric(root1))  # 输出: True

    # 示例2：非对称树
    root2 = build_tree([1, 2, 2, None, 3, None, 3])
    print(Solution().isSymmetric(root2))  # 输出: False