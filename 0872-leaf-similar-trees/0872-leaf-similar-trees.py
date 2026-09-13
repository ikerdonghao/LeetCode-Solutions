# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafSequence(node,seq):
            # if node.left is None and node.right is None:
            if node is None:
                return
            getLeafSequence(node.left,seq)
            getLeafSequence(node.right,seq)
            if node.left is None and node.right is None:
                seq.append(node.val)
            return seq
        seq1 = getLeafSequence(root1,[])
        print(f"seq1 is {seq1}")
        seq2 = getLeafSequence(root2,[])
        print(f"seq2 is {seq2}")
        if seq1 == seq2:
            return True
        else:
            return False