class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # maxheap = []
        # for num in nums:
        #     heapq.heappush(maxheap, -num)
        
        # res = - heapq.heappop(maxheap)
        # while k > 1:
        #     res = - heapq.heappop(maxheap)
        #     k -= 1
        
        # return res
        minheap = nums[:k] # puts in elem until the kth
        heapq.heapify(minheap) # O(k)

        for num in nums[k:]:
            if num > minheap[0]: # compare with smallest, if bigger than smallest
                heapq.heappushpop(minheap, num) # pushes item + pops off smallest

        # root of heap = kth largest
        return minheap[0] #top elem