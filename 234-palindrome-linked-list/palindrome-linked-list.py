# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list1 = []
        curr = head
        while curr:
            list1.append(curr.val)
            curr = curr.next
        print(list1,list1[::-1])
        if list1==list1[::-1]:
            return True
        else:
            return False