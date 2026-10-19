class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # must finish eating 1 pile before movign to next
        # want minimum eating rate to finish in h time k bananas/h
        # calculate length of piles, if n == h, min = largest i
       
        n = len(piles)
        low = 1
        high = max(piles)

        if n == h:
            return high
        
        while low < high:
            mid = (low + high) // 2
            k = mid
            
            total = 0
            for i in piles:
                total += (i + k - 1) // k # equivalent to ceil
            if total <= h:
                high = mid
            else:
                low = mid + 1
        return low
