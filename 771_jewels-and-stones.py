class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        s = 0
        for ch in S:
            if ch in J:
                s += 1

        return s
