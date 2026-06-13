class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            req_val = target - nums[i]

            if req_val in seen:
                return [seen[req_val],i]
            
            seen[nums[i]] = i
        
    
            

    
        