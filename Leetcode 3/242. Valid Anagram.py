class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = {}
        for i in s:
            if i not in c:
                c[i] = 1
            else:
                c[i] += 1
        for i in t:
            if i not in c:
                return( False)
            else:
                c[i] -= 1
                if c[i] < 0:
                    return( False)
        for v in c.values():
            if v!=0:
                return(False)
        return (True)