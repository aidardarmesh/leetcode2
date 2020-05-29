from typing import *

class Solution:
    def nextClosestTime(self, time: str) -> str:
        s = set(''.join(time[:2] + time[3:]))
        
        def hours(s):
            res = []
            
            for h0 in s:
                for h1 in s:
                    hh = h0 + h1
                    
                    if hh <= '23':
                        res.append(h0 + h1)
            
            return res
        
        def minutes(s):
            res = []
            
            for m0 in s:
                for m1 in s:
                    mm = m0 + m1
                    
                    if mm <= '59':
                        res.append(m0 + m1)
            
            return res
        
        times = []
        
        for hh in hours(s):
            for mm in minutes(s):
                times.append(hh + ':' + mm)
        
        times = sorted(times)
        
        for cur_time in times:
            if cur_time > time:
                return cur_time
        
        return times[0]
