from typing import *

class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return chr(257)
        
        return chr(258).join(strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(257):
            return []
        
        return s.split(chr(258))
