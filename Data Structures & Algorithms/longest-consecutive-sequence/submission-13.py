class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        max_streak = 0
        num_set = set(nums)
        streak = 0
        
        for num in num_set:
            streak = 1
            current_num = num

            if num-1 in num_set:
                max_streak = max(max_streak, streak)
                continue

            while current_num+1 in num_set:
                streak += 1
                current_num += 1

            max_streak = max(max_streak, streak)
            

        return max_streak


        