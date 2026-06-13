class Solution:

    def encode(self, strs: List[str]) -> str:
        # we have to encode to a str ,and then decode. 
        encoded = []
        #length#word
        for i in strs:
            word=str(len(i))+ '#' + i
            encoded.append(word)
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+= 1

            length = int(s[i:j])
            i =j+1
            res.append(s[i:i + length])
            i+=length

        return res

