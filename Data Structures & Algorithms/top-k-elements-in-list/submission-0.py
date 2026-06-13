class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        # add freq count. 

        for i in nums:
            freq[i] = freq.get(i , 0) + 1
        
        # now return top k elements . 

        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]
        