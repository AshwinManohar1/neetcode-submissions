class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []

        # sqrt((x1 - x2)^2 + (y1 - y2)^2)

        x2 , y2 = 0, 0

        for coordinate in points:

            x , y = coordinate

            distance = x**2 + y**2

            heapq.heappush(max_heap , (-distance , x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [[x, y] for dist , x, y in max_heap]

