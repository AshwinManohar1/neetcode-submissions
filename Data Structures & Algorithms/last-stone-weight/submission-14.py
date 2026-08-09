class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # convert this to max_heap and pop and push back
        max_heap = [-val for val in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:

            val1 = -heapq.heappop(max_heap)
            val2 = -heapq.heappop(max_heap)

            diff = abs(val1-val2)
            if diff > 0:
                heapq.heappush(max_heap, -diff)
        max_heap.append(0)
        return -max_heap[0]





        