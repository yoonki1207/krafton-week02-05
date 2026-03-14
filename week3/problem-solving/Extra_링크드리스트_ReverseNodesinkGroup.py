# 링크드리스트 - Reverse Nodes in k-Group
# 문제 링크: https://leetcode.com/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional

a = Optional[str]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k += 1
        n = k
        c = 0
        point = head
        cnt = 0
        while point:
            point = point.next
            cnt += 1
        point = head
        tail = head
        ret = head
        prev = None
        isSwitched = False
        while point.next:
            if n == k:
                ret = point
            if n % (k - 1) == 0:
                isSwitched = True
                prev = point
                point = point.next
                tail = point
                if cnt - c < k:
                    break
                n += 1
                c += 1
                continue
            next = point.next
            point.next = next.next
            next.next = tail
            tail = next
            if not isSwitched:
                ret = tail
            if prev:
                prev.next = tail
            n += 1
            c += 1
            pass
        return ret

def cout(node: Optional[ListNode]):
    curr = node
    while curr:
        print(curr.val, end=' ')
        curr = curr.next
    print()

head = ListNode(1)
curr = head
for i in range(2, 11):
    ln = ListNode(i)
    curr.next = ln
    curr = ln
solution = Solution()
tail = solution.reverseKGroup(head, 3)
cout(tail)



