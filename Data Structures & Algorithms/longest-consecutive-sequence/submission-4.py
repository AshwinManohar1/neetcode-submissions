class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # we can sort and left , right 
        # [2, 3, 4, 4, 5, 10 , 20]
        # if len(nums) < 2:
        #     return len(nums)
        # nums.sort()
        # count = set()
        # for right in range(1 ,len(nums)):
        #     if (nums[right] - nums[right - 1]) == 1:
        #         if nums[right] not in count:
        #             count.add(nums[right])
        #         if nums[right-1] not in count:
        #             count.add(nums[right - 1])
        # return len(count)

        if not nums:
            return 0

        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while (current_num + 1) in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(current_streak, longest_streak)

        return longest_streak
        



        