class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            if sum(int(digit) for digit in str(num)) == i:
                return i
        return -1