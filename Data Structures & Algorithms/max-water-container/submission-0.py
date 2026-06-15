class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # when is the maximum water saved:
        # when breadth is more and height is also more. 

        # since bredth and height have to more, we can choose 2 pointers from far away
        # calculate the volume , return the highest
        left = 0
        right = len(heights) -1
        max_volume = 0
        while left < right:
            width = right - left
            height = min(heights[left] , heights[right])
            volume = width * height 
            max_volume= max(volume , max_volume)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1

        return max_volume