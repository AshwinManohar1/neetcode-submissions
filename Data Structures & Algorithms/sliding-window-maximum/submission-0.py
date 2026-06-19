class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_arr= []
        for i in range(len(nums)):
            if i+k <= n:
                new_arr = nums[i:i+k]

                max_ele = max(new_arr)

                max_arr.append(max_ele)

        return max_arr
