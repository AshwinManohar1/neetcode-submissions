# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # dummy = ListNode(0)
        # curr = dummy

        # if list1.val <= list2.val:
        #     curr1 = list1
        #     curr2 = list2
        # else:
        #     curr1 = list2
        #     curr2 = list1

        # while curr1:
        #     if curr1.val <=curr2.val:
        #         curr.val = curr1.val
        #         curr.next = curr2.val
        #     else:
        #         curr.val = curr2.val
        #         curr.next = curr1.val
        #     curr = curr.next
        #     curr1 = curr.next
        #     curr2 = curr.next

        # return dummy.next

        temp = []

        curr = list1
        while curr:
            temp.append(curr.val)
            curr = curr.next

        curr = list2
        while curr:
            temp.append(curr.val)
            curr = curr.next

        temp.sort()

        dummy = ListNode(0)
        curr = dummy

        for val in temp:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next



