from typing import *

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n_letters, line_words = 0, []
        
        for w in words:
            line_words.append(w)
            n_letters += len(w)
            
            if n_letters + len(line_words)-1 > maxWidth:
                line_words.pop()
                n_letters -= len(w)
                
                n_spaces = maxWidth - n_letters
                n_groups = len(line_words)-1
                
                if len(line_words) == 1:
                    line = line_words + [' ' * n_spaces]
                else:
                    right_width = n_spaces // n_groups
                    left_redundant = n_spaces % n_groups
                    left_width = right_width + (1 if left_redundant else 0)
                    spaces = [' ' * left_width] * left_redundant
                    spaces += [' ' * right_width] * (n_groups-left_redundant)
                    spaces += ['']
                    line = [line_words[i] + spaces[i] for i in range(len(line_words))]
                
                res.append(''.join(line))
                n_letters = len(w)
                line_words = [w]
        
        if line_words:
            n_letters = sum([len(w) for w in line_words])
            n_spaces = len(line_words)-1
            res.append(' '.join(line_words) + ' ' * (maxWidth-n_letters-n_spaces))
        
        return res
