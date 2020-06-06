from typing import *

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        rooms = 0
        starts = sorted([x[0] for x in intervals])
        ends = sorted([x[1] for x in intervals])
        e_ptr = 0
        
        for s_ptr in range(len(starts)):
            if starts[s_ptr] >= ends[e_ptr]:
                e_ptr += 1
            else:
                rooms += 1
        
        return rooms
