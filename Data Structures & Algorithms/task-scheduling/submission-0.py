class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        # like tieing the not question. least you can do to store 

        freq = Counter(tasks)

        time = 0

        max_heap = [-val for val in freq.values()]

        heapq.heapify(max_heap)

        cooling_queue = deque()

        while max_heap or cooling_queue:
            time += 1
            if max_heap:
                count = -heapq.heappop(max_heap) - 1
            
                if count > 0:
                    time_at = time+n
                    cooling_queue.append((count , time_at))

            
            if cooling_queue and cooling_queue[0][1] == time:
                ready_count , _ = cooling_queue.popleft()

                heapq.heappush(max_heap , -ready_count)

        return time

