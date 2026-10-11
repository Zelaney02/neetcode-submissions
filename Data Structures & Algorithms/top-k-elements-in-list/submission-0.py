from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep count, sort by frequency, get num
        # keys must be unique and unchanging -> num

        result = []

        c = Counter(nums)
        k_elem = c.most_common(k)

        for num, count in k_elem:
            result.append(num)
        return result

        