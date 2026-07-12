class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:

        self.arr.append(num)
        

    def findMedian(self) -> float:
        
        sorted_arr = sorted(self.arr)

        n = len(sorted_arr)

        mid = n//2

        median = 0
        if n% 2 ==0:
            median = (sorted_arr[mid-1] + sorted_arr[mid]) / 2
        else:
            median = sorted_arr[mid]


        return median


        