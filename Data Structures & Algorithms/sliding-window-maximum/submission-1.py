class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() 
        result = []
        
        for i, num in enumerate(nums):
            # 1. Remove indices that are out of the current window bounds
            if q and q[0] < i - k + 1:
                q.popleft()
                
            # 2. Remove smaller elements from the back as they won't ever be the max
            while q and nums[q[-1]] < num:
                q.pop()
                
            # 3. Add the current element's index
            q.append(i)
            
            # 4. The first element in the queue is always the maximum of the window
            if i >= k - 1:
                result.append(nums[q[0]])
                
        return result