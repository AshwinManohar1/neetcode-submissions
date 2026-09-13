class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def generate_subset(i , curr , total):

            # base

            if total == target:
                res.append(list(curr))
                return 
            
            if total > target or i == len(candidates):
                return 

            
            curr.append(candidates[i])

            generate_subset(i+1 , curr , total+candidates[i])

            curr.pop()

            while i+1< len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            generate_subset(i+1 , curr , total)

        generate_subset(0 , [], 0)

        return [list(combination) for combination in res]
    
       