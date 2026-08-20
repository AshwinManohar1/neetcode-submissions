class Solution:

    def encode(self, strs: List[str]) -> str:
        
        word =""
        for s in strs:
            word+=f"{len(s)}#{s}"

        return word


    def decode(self, s: str) -> List[str]:
        i , j =0, 0
        arr = []
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            
            length = int(s[i:j])
            i= j+1
            word = s[i:i+length]
            arr.append(word)
            i = i+length

        return arr



        

