class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sort and group
        seen = {}

        for s in strs:
            val = "".join(sorted(s))
            if val not in seen:
                seen[val] = []
            
            seen[val].append(s)
            
        return list(seen.values())

        
