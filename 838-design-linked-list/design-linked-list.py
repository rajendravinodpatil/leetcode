class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)  # dummy node
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:  # invalid index
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:  # invalid index
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        # Add newNode between [prev] and [prev.next]
        new_node = ListNode(val, curr.next)
        curr.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:  # invalid index
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        curr.next = curr.next.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)