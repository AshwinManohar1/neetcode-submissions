class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        missing = len(t)
        left = 0
        target_counts = {}
        start , end = 0,0
        for char in t:
            target_counts[char] = target_counts.get(char, 0) + 1

        for right , char in enumerate(s):

            if target_counts.get(char, 0) > 0:
                missing -= 1
            
            target_counts[char] = target_counts.get(char, 0) -1

            while missing == 0:
                if end == 0 or (right - left + 1) < (end - start):
                    start, end = left , right + 1

                target_counts[s[left]] += 1

                if target_counts[s[left]] > 0:
                    missing +=1

                left +=1
            

        return s[start:end]