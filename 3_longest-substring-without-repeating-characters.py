class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # find the repeating chars substrings and use these substrings as break point


        rt = i = j = 0

        n = len(s)

        chars = set()

        while i < n and j < n:
            if s[j] not in chars:
                chars.add(s[j])
                j += 1
                rt = max(rt, len(chars))
            else:
                chars.remove(s[i])
                i += 1

        return rt
