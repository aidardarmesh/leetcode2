from typing import *

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        
        deq = deque()
        deq.append((beginWord, 1))
        visited = set([beginWord])
        wordList = set(wordList)
        
        while deq:
            word, cnt = deq.popleft()
            
            if word == endWord:
                return cnt
            
            for i in range(len(word)):
                for char_id in range(26):
                    new_word = word[:i] + chr(97+char_id) + word[i+1:]
                    
                    if new_word in wordList and not new_word in visited:
                        deq.append((new_word, cnt+1))
                        visited.add(new_word)
            
        return 0
