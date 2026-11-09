class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # store the freq for 1 word , keep reducing or removing the charcter the frq , ill check the length of freq , at the end if not zero then not a anagram. 
        freq = {}

        if len(s) != len(t):
            return False

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        
        for char in t:
            if char in freq:
                freq[char] -= 1

                if freq[char] == 0:
                    del freq[char]

        return len(freq) == 0
        
            
        
     