class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_val = "".join(char.lower() for char in s if char.isalnum())

        left = 0
        right = len(new_val) - 1

        while left < right:
            if new_val[left] != new_val[right]:
                return False
            left += 1
            right -= 1

        return True