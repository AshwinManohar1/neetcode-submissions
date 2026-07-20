class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        length = n*2
        numbers = [""] * length

        def solve(index, total):
            if total < 0 or total >  n or index > length:
                return
            
            if index == length:
                if total == 0:
                    result.append("".join(numbers))
                return

            numbers[index] = '('
            solve(index+1, total+1)

            numbers[index] = ')'
            solve(index+1, total-1)

            
        solve(0,0)

        return result
            
            
