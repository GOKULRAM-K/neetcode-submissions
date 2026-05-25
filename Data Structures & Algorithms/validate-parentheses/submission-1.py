class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i in "({[":
                l.append(i)
            else:
                if len(l)==0:
                    return False
                if i == ")":
                    if l[-1]=="(":
                        l.pop()
                        continue
                    else:
                        return False
                elif i == "}":
                    if l[-1]=="{":
                        l.pop()
                        continue
                    else:
                        return False
                elif i == "]":
                    if l[-1]=="[":
                        l.pop()
                        continue
                    else:
                        return False
        if len(l)!=0:
            return False
        return True