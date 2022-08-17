# Definition for singly-linked list.

#i dont know why its not working here????


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
head = [3,2,0,-4]
pos = 1
class Solution:
    def hasCycle(self, head) -> bool:
        slow,fast = head,head

        while fast and fast.next:
            slow =slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


a =Solution()
print(a.hasCycle(head))
        