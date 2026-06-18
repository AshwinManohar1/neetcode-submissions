class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # instead of hash need to check the s1 variable.
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        freq_s1 = {}
        freq_2 = {}
        
        # 1. Build freq_s1 AND populate freq_2 with the FIRST window
        for i in range(n1):
            freq_s1[s1[i]] = freq_s1.get(s1[i], 0) + 1
            freq_2[s2[i]] = freq_2.get(s2[i], 0) + 1

        if freq_s1 == freq_2:
            return True

        for i in range(n1 , n2):

            right_char = s2[i]

            freq_2[right_char] = freq_2.get(right_char , 0) + 1

            left_char = s2[i - n1]
            freq_2[left_char] -= 1

            if freq_2[left_char] == 0:
                del freq_2[left_char]

            if freq_2 == freq_s1:
                return True
        
        return False
            
            