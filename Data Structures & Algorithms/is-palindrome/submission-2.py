class Solution:
    def isPalindrome(self, s: str) -> bool:
        # to check palindrome , need to check left to right eauls right to left

        left = 0
        new_var = "".join([char.lower() for char in s if char.isalnum()])

        right = len(new_var) - 1

        while left <= right:
            if new_var[left] != new_var[right]:
                return False
            left += 1
            right -= 1

        return True
        