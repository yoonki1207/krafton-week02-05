# 트리, BFS - Binary Tree Level Order Traversal
# 문제 링크: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, roots):
        if not roots: return []
        level_nodes = []
        for node in roots:
            if node.left: level_nodes.append(node.left)
            if node.right: level_nodes.append(node.right)
        rets = self.solve(level_nodes)
        if rets:
            return [roots] + rets
        else:
            return [roots]
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ret = self.solve([root])
        arr = []
        for lst in ret:
            lst = [i.val for i in lst]
            arr.append(lst)
        return arr