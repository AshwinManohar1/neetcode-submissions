class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num_needed = target - nums[i]

            if num_needed in seen:
                return [seen[num_needed],i]
            else:
                seen[nums[i]] = i

        return [-1 , -1]

    
            

    
        