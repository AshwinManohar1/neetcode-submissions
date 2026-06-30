class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        min_speed = right

        while left <= right:
            mid_speed = left + (right - left) //2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/mid_speed)

            if total_time <= h:
                min_speed = mid_speed
                right = mid_speed - 1
            else:
                left = mid_speed + 1

        
        return min_speed