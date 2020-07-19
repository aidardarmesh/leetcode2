from typing import *

class Codec:
    LEN_SEP = '_'
    META_DATA_SEP = '|'
  
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        lens = self.LEN_SEP.join([str(len(word)) for word in strs])
        data = ''.join(strs)

        return lens + self.META_DATA_SEP + data


    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        meta_data_sep_idx = s.find(self.META_DATA_SEP)
	
        if not meta_data_sep_idx:
            return []

        lens, data = s[:meta_data_sep_idx], s[meta_data_sep_idx+1:]
        lens = lens.split(self.LEN_SEP)

        ans = []
        start_idx = 0

        for word_len in lens:
            end_idx = start_idx + int(word_len)
            ans.append(data[start_idx:end_idx])
            start_idx = end_idx

        return ans
