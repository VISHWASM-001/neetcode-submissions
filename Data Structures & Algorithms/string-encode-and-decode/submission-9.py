class Solution:

    def encode(self, strs: List[str]) -> str:
       str =""
       for i in strs:
        str+=i
        str+="~"

       return str 


    def decode(self, s: str) -> List[str]:
        a = s.split("~")
        a.pop()

        return a
        
