# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next

        # temp = []

        # curr = list1
        # while curr:
        #     temp.append(curr.val)
        #     curr = curr.next

        # curr = list2
        # while curr:
        #     temp.append(curr.val)
        #     curr = curr.next

        # temp.sort()

        # dummy = ListNode(0)
        # curr = dummy

        # for val in temp:
        #     curr.next = ListNode(val)
        #     curr = curr.next

        # return dummy.next



