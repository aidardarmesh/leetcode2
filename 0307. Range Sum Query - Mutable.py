from typing import *

class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        
        self.nums = nums
        self.n = len(nums)
        self.st = [0] * 4 * self.n
        self.temp = [0] * 4 * self.n
        self._build(0, 0, self.n-1)
    
    def _push(self, v, vl, vr):
        if vl != vr:
            self.temp[2*v+1] += self.temp[v]
            self.temp[2*v+2] += self.temp[v]
        
        self.st[v] += self.temp[v] * (vr-vl+1)
        self.temp[v] = 0
    
    def _build(self, v, vl, vr):
        if vl == vr:
            self.st[v] = self.nums[vl]
            return
        
        vm = vl + (vr-vl) // 2
        self._build(2*v+1, vl, vm)
        self._build(2*v+2, vm+1, vr)
        self.st[v] = self.st[2*v+1] + self.st[2*v+2]
    
    def _query(self, v, vl, vr, l, r):
        self._push(v, vl, vr)
        
        if vl > r or vr < l:
            return 0
        
        if l <= vl and vr <= r:
            return self.st[v]
        
        vm = vl + (vr-vl) // 2
        ql = self._query(2*v+1, vl, vm, l, r)
        qr = self._query(2*v+2, vm+1, vr, l, r)
        
        return ql + qr
    
    def _update(self, v, vl, vr, l, r, val):
        self._push(v, vl, vr)
        
        if vl > r or vr < l:
            return
        
        if l <= vl and vr <= r:
            self.st[v] = val
            return
        
        vm = vl + (vr-vl) // 2
        self._update(2*v+1, vl, vm, l, r, val)
        self._update(2*v+2, vm+1, vr, l, r, val)
        self.st[v] = self.st[2*v+1] + self.st[2*v+2]
    
    def update(self, i: int, val: int) -> None:
        self._update(0, 0, self.n-1, i, i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self._query(0, 0, self.n-1, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)