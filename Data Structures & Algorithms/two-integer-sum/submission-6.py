class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        


        seen = {}

        for i in range(len(nums)):

            required_num = target - nums[i]

            if required_num in seen:
                return [seen[required_num], i]
            
            seen[nums[i]] = i

            
        
    
            

    
        