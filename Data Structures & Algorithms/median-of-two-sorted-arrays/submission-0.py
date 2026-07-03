class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        n = len(nums1)
        m = len(nums2)
        median = 0
        arr = [0] * (m + n)

        for i in range(n):
            arr[i] = nums1[i] 

        for j in range(m):
            arr[n+j] = nums2[j]
        
        arr.sort()

        length = len(arr)
        if length % 2 == 0:
            index1 = length // 2 
            index2 = (length -1 ) // 2
            median = (arr[index1] + arr[index2]) / 2
        else:

            index = length // 2
            median = arr[index]

        return median

        



