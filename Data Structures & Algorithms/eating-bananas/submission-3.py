class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        min_speed = max(piles)
        right = min_speed
        while left <= right:

            mid = (left + (right - left) // 2)
            time_taken = 0
            for val in piles:
                time_taken+= math.ceil(val/mid)
            
            if time_taken <= h:
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1


        
        return min_speed