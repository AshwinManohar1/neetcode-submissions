class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # if not nums:
        #     return 0

        # longest_streak = 0

        # for num in nums:
        #     current_num = num
        #     current_streak = 1

        #     while (current_num + 1) in nums:
        #         current_num += 1
        #         current_streak += 1

        #     longest_streak = max(current_streak, longest_streak)

        # return longest_streak
        
        if not nums:
            return 0

        nums_set = set(nums)
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            if current_num - 1 in nums_set:
                longest_streak = max(current_streak,longest_streak)
                continue

            while current_num + 1 in nums_set: 
                # sequence starter.
                current_num +=1
                current_streak += 1
            
            longest_streak = max(current_streak,longest_streak)

        return longest_streak
            



        