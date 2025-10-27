class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        st=set()
        has={}
        for i in range(len(s)):
            x=s[i:i+10]
            if x in has:
                st.add(x)
            else:
                has[x]=0

        return list(st)
        