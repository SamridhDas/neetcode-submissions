"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        finish=float("-inf")
        for interval in  intervals:
            if interval.start<finish:
                return False
            finish=interval.end
        return True

