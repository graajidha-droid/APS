class Solution:
    def countCommas(self, n: int) -> int:
        count=0
        k=1000
        while k<=n:
            count+=n-k+1
            k*=1000
        return count