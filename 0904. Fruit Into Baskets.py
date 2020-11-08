from typing import *

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = 0
        left = 0
        baskets = collections.defaultdict(int)
        
        for right in range(len(tree)):
            baskets[tree[right]] += 1
            
            while len(baskets) > 2:
                baskets[tree[left]] -= 1
                
                if baskets[tree[left]] == 0:
                    del baskets[tree[left]]
                
                left += 1
            
            res = max(res, right-left+1)
        
        return res
