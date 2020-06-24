from typing import *

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        def rand49():
            return (rand7()-1)*7 + rand7()
        
        while True:
            rand_val = rand49()
            
            if rand_val <= 40:
                return rand_val % 10 + 1
