from collections import Counter

class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        freq = Counter(digits)
        valid_count = 0

        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            req = Counter([d1, d2, d3])

            if all(freq[d] >= req[d] for d in req):
                valid_count += 1

        return valid_count