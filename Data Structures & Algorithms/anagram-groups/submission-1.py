class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq ={}

        for s in strs:
            new_s = "".join(sorted(s))

            if new_s not in freq:
                freq[new_s] = []
        
            freq[new_s].append(s)

        return list(freq.values())

