class Solution:
    def isValid(self, s: str) -> bool:
        d = {")":"(", "}":"{", "]":"["}
        l = []

        for i in s:
            if i in "([{":
                l.append(i)
            else:
                if len(l)==0:
                    return False
                if l[-1] != d[i]:
                    return False
                else:
                    l.pop()
        if len(l)!=0:
            return False
        return True