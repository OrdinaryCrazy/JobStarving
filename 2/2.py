# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p, q = l1, l2
        out = None
        cur = None
        inc_flag = 0
        while p and q:
            if cur is None:
                cur = ListNode((p.val + q.val + inc_flag) % 10)
                inc_flag = (p.val + q.val + inc_flag) // 10
                out = cur
                p = p.next
                q = q.next
                continue
            cur.next = ListNode((p.val + q.val + inc_flag) % 10)
            inc_flag = (p.val + q.val + inc_flag) // 10
            cur = cur.next
            p = p.next
            q = q.next
        while p:
            cur.next = ListNode((p.val + inc_flag) % 10)
            inc_flag = (p.val + inc_flag) // 10
            cur = cur.next
            p = p.next
        while q:
            cur.next = ListNode((q.val + inc_flag) % 10)
            inc_flag = (q.val + inc_flag) // 10
            cur = cur.next
            q = q.next
        if inc_flag:
            cur.next = ListNode(inc_flag)
        return out
            