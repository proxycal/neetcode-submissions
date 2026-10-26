class Solution:

    def encode(self, strs: List[str]) -> str:
        stri=""
        for i in strs:
            stri+=str(len(i))+'#'+i
        return stri

    def decode(self, s: str) -> List[str]:
        position=0
        hold=[]
        while position<len(s):
            indi= s.find("#",position)
            leg=int(s[position:indi])
            extract=s[indi+1:leg+indi+1]
            hold.append(extract)
            position=leg+indi+1
        return hold






