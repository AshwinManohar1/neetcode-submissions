class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.points = points
        self.k = k

        self.max_heap = []
        

        for coordinate in self.points:
            x, y = coordinate

            distance = x**2+y**2

            heapq.heappush(self.max_heap , (-distance , x , y))

            if len(self.max_heap) > self.k:
                heapq.heappop(self.max_heap)

        return [[x, y] for distance , x, y in self.max_heap]
      
      


