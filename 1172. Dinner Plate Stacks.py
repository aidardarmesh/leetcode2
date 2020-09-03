from typing import *

class DinnerPlates:

    def __init__(self, capacity: int):
        import heapq
        self.cap = capacity
        self.stacks = []
        self.abl = []

    def push(self, val: int) -> None:
        while self.abl and self.abl[0] < len(self.stacks) and len(self.stacks[self.abl[0]]) == self.cap:
            heapq.heappop(self.abl)

        if not self.abl:
            heapq.heappush(self.abl, len(self.stacks))

        if self.abl[0] == len(self.stacks):
            self.stacks.append([])

        self.stacks[self.abl[0]].append(val)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        
        return self.popAtStack(len(self.stacks)-1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index and index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.abl, index)
            return self.stacks[index].pop()
        
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)