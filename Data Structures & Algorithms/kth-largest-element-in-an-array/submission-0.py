class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # put all elements from array into heap + sort
        maxheap = []
        for num in nums:
            heapq.heappush(maxheap, -num)
        
        res = - heapq.heappop(maxheap)
        while k > 1:
            res = - heapq.heappop(maxheap)
            k -= 1
        
        return res
