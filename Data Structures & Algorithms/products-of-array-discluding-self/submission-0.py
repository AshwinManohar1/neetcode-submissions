class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            #ill get the nums , i want to calculate the sum leaving the number
            output = []
            for index , number in enumerate(nums):
                curr_sum = 1
                for i in range(len(nums)):
                    if index == i:
                        continue;
                    
                    curr_sum *= nums[i]
                    
                output.append(curr_sum)

            return output




            