#本题借助大模型
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = TreeNode(val)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return node
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                temp = self._min_value_node(node.right)
                node.val = temp.val
                node.right = self._delete(node.right, temp.val)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        result = []
        if node:
            result = self._inorder_traversal(node.left)
            result.append(node.val)
            result = result + self._inorder_traversal(node.right)
        return result

# 给定数组
nums = [9, -3, -10, 0, 9, 7, 33]
bst = BST()

# 建立二叉搜索树
for num in nums:
    bst.insert(num)

# 删除元素“0”
bst.delete(0)

# 中序遍历输出二叉搜索树中的所有元素
result = bst.inorder_traversal()
print(result)