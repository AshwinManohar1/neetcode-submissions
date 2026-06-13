class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # we know how to chcek anagram, but given that it's already anagram , 
        # we just have to group them . 

        # we can group by the length of the anagrams. 

        seen = {}
        for i in strs:
            new = "".join(sorted(i))

            if new not in seen:
                seen[new]= []

            seen[new].append(i)

        return list(seen.values())