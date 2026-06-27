class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # freq = {}

        # for num in nums:
        #     freq[num] = freq.get(num , 0) + 1

        #     if freq[num] > 1:
        #         return num

        for i in range(len(nums)):
            target_index = abs(nums[i]) - 1
            if nums[target_index] < 0:
                return abs(nums[i])
            nums[target_index] *= -1
            
            

            



