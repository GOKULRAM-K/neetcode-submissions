class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        b = 1
        e = max(piles)
        mid = (b + e) // 2

        min_k = float('inf')
        while (b <= e):
            h_ = 0
            for i in piles:
                h_ += i // mid
                if i%mid>0:
                    h_ += 1
            
            if h_ <= h:
                e = mid - 1
                min_k = min(min_k, mid)
            elif h_ > h:
                b = mid + 1
            


            mid = (b + e) // 2

            
        return min_k