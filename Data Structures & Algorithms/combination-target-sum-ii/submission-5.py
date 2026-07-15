class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        current_combination = []
        candidates.sort()
        def dfs(start_index , current_sum):

            if current_sum == target:
                res.append(current_combination.copy())
                return 

            if current_sum > target:
                return

            for i in range(start_index , len(candidates)):

                if i> start_index and candidates[i] == candidates[i-1]:
                    continue

                current_combination.append(candidates[i])
                dfs(i+1 , current_sum + candidates[i])

                current_combination.pop()


        dfs(0 , 0)
        return res