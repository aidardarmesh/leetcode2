from typing import *

class ProductOfNumbers:

    def __init__(self):
        self.dp = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.dp = [1]
        else:
            self.dp.append(self.dp[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.dp):
            return 0
        
        return self.dp[-1] // self.dp[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
