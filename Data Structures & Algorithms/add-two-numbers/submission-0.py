# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # bruteforce
        arr1 =[]
        arr2 = []

        curr = l1
        while curr:
            arr1.append(str(curr.val))
            curr = curr.next

        curr = l2
        while curr:
            arr2.append(str(curr.val))
            curr = curr.next
        arr1.reverse()
        arr2.reverse()
        val1 = "".join(arr1)    
        val2 = "".join(arr2)
        total = int(val1) + int(val2)
        digits = [int(i) for i in str(total)]
        digits.reverse()
        dummy = ListNode(0)
        curr = dummy

        for val in digits:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next


        
        

        