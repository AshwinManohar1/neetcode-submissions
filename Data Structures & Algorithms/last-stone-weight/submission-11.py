class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # convert this to max_heap and pop and push back
        max_heap = [-val for val in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            val1 = -heapq.heappop(max_heap)
            val2 = -heapq.heappop(max_heap)

            if val1 == val2:
                continue

            if val1 > val2:
                balance = val1 - val2
                heapq.heappush(max_heap, -balance)

        return -max_heap[0] if max_heap else 0
                





        