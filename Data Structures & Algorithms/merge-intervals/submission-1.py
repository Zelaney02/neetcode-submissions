class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        result = []
        if n == 1:
            return intervals
        intervals.sort(key = lambda x:x[0]) # sort by first key
        start = intervals[0][0]
        curr_f = intervals[0][1]
        #if idx_f >= next_idx_s => merge take append(idx_s, next_idx_f), update finish
        for i in range(1, len(intervals)):
            if curr_f >= intervals[i][0]:
                curr_f = max(intervals[i][1], curr_f)
            else:
                result.append([start, curr_f])
                start = intervals[i][0]
                curr_f = intervals[i][1]
        result.append([start, curr_f])
        return result