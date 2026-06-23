class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target - position / speed
        n = len(position)
        fleet = 0

        stack = []
        output = []

        pairs= list(zip(position , speed))

        sorted_cars = sorted(pairs , reverse =True)

        for pos_index, speed in sorted_cars:

            time = (target - pos_index) / speed

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
            