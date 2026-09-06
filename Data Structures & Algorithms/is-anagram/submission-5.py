class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = len(s)
        m = len(t)

        if n != m:
            return False

        freq = {}

        for i in range(n):
            freq[s[i]] = freq.get(s[i], 0) + 1

        
        for i in range(m):
            if t[i] in freq:
                freq[t[i]] -= 1

                if freq[t[i]] == 0:
                    del freq[t[i]]
            else:
                return False

            

        return len(freq) == 0
        
            
        
     