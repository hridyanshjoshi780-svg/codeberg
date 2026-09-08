class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        p = 1000  # Start at 1,000 (10^3)
        
        while n >= p:
            # Add 1 comma for every number >= p
            ans += (n - p + 1)
            p *= 1000
            
        return ans