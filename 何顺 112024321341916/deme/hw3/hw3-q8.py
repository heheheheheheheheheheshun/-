#此题借助大模型
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        显式中序遍历，定位错误节点并交换值
        """
        nodes = []
        self.inorder(root, nodes)  # 中序遍历得到节点列表

        # 定位错误节点
        x, y = None, None
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                y = nodes[i + 1]  # 第二个错误节点
                if x is None:
                    x = nodes[i]  # 第一个错误节点
                else:
                    break  # 已经找到两对逆序

        # 交换节点值
        if x and y:
            x.val, y.val = y.val, x.val

    def inorder(self, root, nodes):
        """中序遍历辅助函数"""
        if not root:
            return
        self.inorder(root.left, nodes)
        nodes.append(root)
        self.inorder(root.right, nodes)


# 测试代码
def build_tree(vals):
    """根据列表构建二叉树（None表示空节点）"""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def print_tree(root):
    """层次遍历打印树结构"""
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    # 去除末尾多余的None
    while res and res[-1] is None:
        res.pop()
    return res


#e.g1
root1 = build_tree([1, 3, None, None, 2])
Solution().recoverTree(root1)
print("示例1输出:", print_tree(root1))

#e.g2
root2 = build_tree([3, 1, 4, None, None, 2])
Solution().recoverTree(root2)
print("示例2输出:", print_tree(root2))