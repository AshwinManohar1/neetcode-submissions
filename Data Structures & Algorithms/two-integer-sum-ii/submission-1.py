class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # because it is sorted and usually the bigger nums are at the end and we need to find a pair
        # 2 pointer with oppposite direction. 

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left +1 , right +1 ]
            elif total < target:
                left += 1
            else:
                right -= 1

        return [-1 , -1]
        