class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i, char in enumerate(s, 1):
            rev_alphabet_pos = 123 - ord(char)  # 'a' (97) -> 26, ..., 'z' (122) -> 1
            ans += rev_alphabet_pos * i
        return ans