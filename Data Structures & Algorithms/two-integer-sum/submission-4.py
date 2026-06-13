class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # left = 0
        # curr_sum = 0

        # for right in range(1, len(nums)):
        #     curr_sum = nums[left] + nums[right] 
        #     if (curr_sum == target):
        #         return [left , right]
        #     curr_sum -= nums[left]
        #     left += 1

        # return [-1 , -1]

    # Sliding window won't work here , as the solution may never be together. 
    # hence we will have to move to 2 pointer. 
        # n =len(nums)
        # left = 0
        # right = n-1
        # while left < right:
        #     total = nums[left] + nums[right]
        #     if total == target:
        #         return [left , right]
        #     elif total < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return [-1 , -1]
        seen = {}
        for i in range(len(nums)):
            req_val = target - nums[i]

            if req_val in seen:
                return [seen[req_val],i]
            
            seen[nums[i]] = i
        
    
            

    
        