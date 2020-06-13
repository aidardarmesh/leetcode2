from typing import *

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        from collections import defaultdict

        cnt = defaultdict(int)
        cnt[0] = 1

        for n in nums:
            step = defaultdict(int)
            
            for inter_sum in cnt:
                step[inter_sum + n] += cnt[inter_sum]
                step[inter_sum - n] += cnt[inter_sum]

            cnt = step
        
        return cnt[S]
