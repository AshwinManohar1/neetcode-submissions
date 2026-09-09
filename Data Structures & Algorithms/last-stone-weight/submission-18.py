class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #conver to max heap

        max_heap = [-val for val in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:

            val1 = -heapq.heappop(max_heap)
            val2 = -heapq.heappop(max_heap)

            balance = val1 - val2

            if balance > 0:
                heapq.heappush(max_heap, -balance)
        max_heap.append(0)
        return -max_heap[0]





        