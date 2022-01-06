# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def mergeTwoLists(p: ListNode, q: ListNode) -> ListNode:
            root = ListNode()
            cur = root
            while p and q:
                if p.val < q.val:
                    cur.next = p
                    p = p.next
                    cur = cur.next
                else:
                    cur.next = q
                    q = q.next
                    cur = cur.next
            # while p:
            #     cur.next = p
            #     p = p.next
            #     cur = cur.next
            # while q:
            #     cur.next = q
            #     q = q.next
            #     cur = cur.next
            if p:
                cur.next = p
            if q:
                cur.next = q
            return root.next
        
        mergedLists = lists
        tempLists = []
        while(len(mergedLists) > 1):
            for i in range(0, len(mergedLists) - 1, 2):
                tempLists.append(mergeTwoLists(mergedLists[i], mergedLists[i + 1]))
            if len(mergedLists) % 2 > 0:
                tempLists.append(mergedLists[-1])
            mergedLists = tempLists
            tempLists = []
        return mergedLists[0]