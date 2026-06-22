class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output=[0] * n

        stack = []

        for curr_day in range(n):

            curr_temp = temperatures[curr_day]


            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()

                output[prev_day] = curr_day - prev_day

            stack.append(curr_day)

        return output








        return output