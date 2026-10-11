from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_data = defaultdict(list)
        

        for s in strs:
            count = [0] * 26 # since only lowercase
            # convert c into a tuple so we can use as key
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            key = tuple(count)
            grouped_data[key].append(s)

        return list(grouped_data.values())
            
