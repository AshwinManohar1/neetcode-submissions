class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicate = False
        freq = {}
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if freq[nums[right]] > 1:
                has_duplicate = True

            
        return has_duplicate
