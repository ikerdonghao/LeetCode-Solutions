# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root.val == 0:
            return [0]
        else:
            self.cur_val = None
            self.cur_freq = 0
            self.max_freq = 0
            self.max_list = []
            def dfs(node:TreeNode):
                if not node:
                    return

                dfs(node.left)
                                
                if node.val != self.cur_val:
                    self.cur_val = node.val
                    self.cur_freq = 1
                else:
                    self.cur_freq += 1

                if self.cur_freq > self.max_freq:
                    self.max_freq = self.cur_freq
                    self.max_list = [self.cur_val]
                elif self.cur_freq == self.max_freq:
                    self.max_list.append(node.val)
                
                dfs(node.right)

            
            dfs(root)
            return self.max_list