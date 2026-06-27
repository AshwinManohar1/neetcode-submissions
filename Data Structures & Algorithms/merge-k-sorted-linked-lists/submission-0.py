# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for list_node in lists:
            curr = list_node
            while curr:
                arr.append(curr.val)
                curr = curr.next

        arr.sort()
        dummy =ListNode(0)
        curr = dummy

        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next

            
        