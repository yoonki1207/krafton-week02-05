# 트리 - Binary Tree Maximum Path Sum
# 문제 링크: https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = -987654321

    def maxPathSumHelp(self, root: Optional[TreeNode]) -> int:
        if not root: return None
        if not root.left and not root.right: # Base condition
            self.ans = max(self.ans, root.val)
            return root.val

        left_info  = self.maxPathSumHelp(root.left)
        right_info = self.maxPathSumHelp(root.right)
        contain_max = root.val
        begin_max = root.val

        if left_info:
            contain_max = max(contain_max, contain_max + left_info)
            begin_max = max(begin_max, root.val + left_info)
        if right_info:
            contain_max = max(contain_max, contain_max + right_info)
            begin_max = max(begin_max, root.val + right_info)
        
        self.ans = max(contain_max, self.ans)

        return begin_max

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        노드의 자식 노드의 정보를 활용할 수 있었으면 좋겠다.
        노드의 자식 노드의 정보는 재귀적으로 구할 수 있을 것 같다.
        노드의 자식 노드로부터 시작하는 최대값을 구할 수 있다면 그게 정답이지 않을까
        루트를 포함하여 왼쪽 오른쪽 서브트리의 루트를 포함한 최대 path
        루트에는 두 가지 추가 상태가 있다.
        루트에서 시작하는 max path
        루트를 포함하는 max path
        '''

        root_ret = self.maxPathSumHelp(root)
        self.ans = max(self.ans, root_ret)
        return self.ans
        