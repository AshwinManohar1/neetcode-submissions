class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return len(stones)

        if len(stones) <= 1:
            return stones[0]

        max_heap = [-1*n for n in stones]

        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x != y:
                heapq.heappush(max_heap, -(x-y))
        
        return -max_heap[0] if max_heap else 0

        