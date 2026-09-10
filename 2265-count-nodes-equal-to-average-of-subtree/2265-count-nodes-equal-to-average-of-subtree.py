# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1
        
        def sumTree(node):
            if node is None:
                return 0
            return node.val + sumTree(node.left) + sumTree(node.right)
        
        def countTreeNode(node):
            if node is None:
                return 0
            else:
                return 1+countTreeNode(node.left)+countTreeNode(node.right)
        
        # print(f"tree_sum is {sumTree(root)}, tree_node_count is {countTreeNode(root)}")

        avg_value = sumTree(root) // countTreeNode(root)

        if avg_value == root.val:
            return 1+self.averageOfSubtree(root.left)+self.averageOfSubtree(root.right)
        else:
            return self.averageOfSubtree(root.left)+self.averageOfSubtree(root.right)