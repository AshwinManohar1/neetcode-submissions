class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"

        return encoded



    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        while i < len(s):
            j = i 

            while s[j] != '#':
                j += 1

            length = s[i:j]
            length = int(length)
            i=j+1
            res.append(s[i:i+length])
            i = i+length

        return res
        

