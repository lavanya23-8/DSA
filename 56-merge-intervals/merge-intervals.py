class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        merged.append(intervals[0])
        
        for i in range(1, len(intervals)):
            current = intervals[i]
            last = merged[-1]
            
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        
        return merged
