# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # arr = []
        # for list_node in lists:
        #     curr = list_node
        #     while curr:
        #         arr.append(curr.val)
        #         curr = curr.next

        # arr.sort()
        # dummy =ListNode(0)
        # curr = dummy

        # for val in arr:
        #     curr.next = ListNode(val)
        #     curr = curr.next

        # return dummy.next

        if not lists or len(lists) == 0:
            return None

        def mergeTwoLists(l1 , l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2

            return dummy.next


        while len(lists) > 1:
            merged_pairs = []


            for i in range(0 , len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_pairs.append(mergeTwoLists(l1 , l2))

            lists = merged_pairs

        
        return lists[0]
            

            
        