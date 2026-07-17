class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        current_combination = []
        nums.sort()

        def dfs(start_index):

            results.append(current_combination.copy())

            for i in range(start_index , len(nums)):

                if i > start_index and nums[i] == nums[i-1]:
                    continue

                current_combination.append(nums[i])
                dfs(i+1)

                current_combination.pop()
        
        dfs(0)
        return results




            
            


