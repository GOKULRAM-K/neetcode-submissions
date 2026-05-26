class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i not in "*-+/":
                s.append(i)
            else:
                n2 = int(s.pop())
                n1 = int(s.pop())
                if i == "*":
                    r = n1*n2
                elif i == "+":
                    r = n1+n2
                elif i == "-":
                    r = n1-n2
                else:
                    r = int(n1/n2)
                s.append(r)
        return int(s[0])