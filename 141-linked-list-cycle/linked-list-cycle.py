# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False
        # if head==None or head.next==None:
        #     return False
        # dummy = ListNode(0)
        # dummy.next = head
        # slow = dummy
        # fast = slow.next 
        # while slow and fast.next and fast:
        #     print("slow ==>",slow.val)
        #     print("fast ==>",fast.val)
        #     slow=slow.next
        #     fast=fast.next.next
        #     if slow==fast:
        #         return True
        # return False
        # visited_node = set()
        # curr = head
        # while curr:
        #     if curr.val in visited_node:
        #         return True
        #     visited_node.add(curr.val)
        #     curr = curr.next
        # return False
        # print(head)
        # if head is not None:
        #     dummy = ListNode(0)
        #     dummy.next = head
        #     slow = dummy
        #     fast = slow.next

        #     while fast.next and fast:
        #         slow=slow.next
        #         fast=fast.next.next
        #         if slow==fast:
        #             return True
        #     return False
        # else:
        #     return False  