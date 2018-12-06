from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """

        deck2 = sorted(deck)

        rt = deque([])

        while len(deck2) > 1:
            rt.appendleft(deck2.pop())
            rt.appendleft(rt.pop())

        rt.appendleft(deck2.pop())
        return list(rt)


if __name__ == "__main__":
    print(Solution().deckRevealedIncreasing([1, 2, 3]))
