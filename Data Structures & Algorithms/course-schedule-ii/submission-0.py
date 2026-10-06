class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        pre_req = {i : [] for i in range(numCourses)}

        visited , cycle = set(), set()

        order = []

        for crs , pre in prerequisites:
            pre_req[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)
            for cre in pre_req[crs]:
                if dfs(cre) == False:
                    return False 
                
            cycle.remove(crs)
            visited.add(crs)
            order.append(crs)

            return True

        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []

        return order

