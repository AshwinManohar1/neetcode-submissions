class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {']':'[', '}': '{', ')':'('}

        for ch in s:
            if ch in match.values():
                stack.append(ch)

            else:
                if not stack or stack.pop() != match[ch]:
                    return False

        return not stack
        