class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m: # if length does not match it's false. 
            return False
        freq= {}
        is_anagram= True

        # adding freq count to dict.
        for i in range(n):
            freq[s[i]] = freq.get(s[i], 0) + 1

        
        # check if variable exists
        for j in range(m):
            has_val = t[j] in freq
            if not has_val:
                is_anagram = False
            else:
                freq[t[j]] =freq.get(t[j]) - 1
                if freq[t[j]] == 0:
                    del freq[t[j]]
            
        
        return is_anagram