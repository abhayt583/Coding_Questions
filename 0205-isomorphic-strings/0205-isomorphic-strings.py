class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ss={}
        tt={}

        for a,b in zip( s,t):
            if a in ss:
                if ss[a]!=b:
                    return False
            else:
                ss[a]=b
            if b in tt:
                if tt[b]!=a:
                    return False
            else:
                tt[b]=a
        return True

        

        