class Solution:

    def encode(self, strs: List[str]) -> str:
        
        word = ""

        for s in strs:
            word+=f"{len(s)}#{s}"

        return word 


    def decode(self, s: str) -> List[str]:
        
        i = 0
        arr = []
        
        while i < len(s):

            j = i

            while s[j] != '#':
                j+=1

            length = int(s[i:j])
            start_of_word = j+1
            end_of_word= start_of_word + length

            word = s[start_of_word:end_of_word]
            arr.append(word)

            i = end_of_word

        return arr


        

