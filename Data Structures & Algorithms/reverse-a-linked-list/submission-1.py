# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # curr = head
        # temp = []

        # while curr:
        #     temp.append(curr.val)
        #     curr = curr.next

        # temp.reverse()


        # dummy = ListNode(0)

        # curr = dummy

        # for val in temp:
        #     curr.next = ListNode(val)
        #     curr = curr.next 

        # return dummy.next

        prev = None
        curr = head

        while curr:

            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        return prev

        

            

        