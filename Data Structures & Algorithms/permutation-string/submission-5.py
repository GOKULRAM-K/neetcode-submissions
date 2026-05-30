class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        
        for i in range(len(s1)):
            d[s1[i]] = d.get(s1[i], 0) + 1

        for i in range(len(s2)-len(s1)+1):
            w = {}
            for j in range(len(s1)):
                w[s2[i+j]] = w.get(s2[i+j], 0) + 1
            if w == d:
                return True
        return False