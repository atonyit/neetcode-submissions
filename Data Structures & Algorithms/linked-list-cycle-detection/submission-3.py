# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        my_set = set()
        curr = head

        while curr:
            if curr in my_set:
                return True
            my_set.add(curr)
            curr = curr.next
        return False
        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        #     if slow == fast:
        #         return True
 
        # return False