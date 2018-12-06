
class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        left = [1 for _ in range(len(A))]
        right = [1 for _ in range(len(A))]

        stack = []
        for i in range(len(A)):
            while stack and stack[-1][1] > A[i]:
                stack.pop()

            left[i] = i+1 if not stack else (i - stack[-1][0])
            stack.append((i, A[i]))

        stack = []
        for i in range(len(A)):
            j = len(A) - i - 1
            while stack and stack[-1][1] >= A[j]:
                stack.pop()
            right[j] = (len(A) - j) if not stack else (stack[-1][0] - j)
            stack.append((j, A[j]))

        rt = 0
        for i in range(len(A)):
            rt += (A[i] * left[i] * right[i])

        return rt % ((10**9)+7)


if __name__ == "__main__":
    print(Solution().sumSubarrayMins([71,55,82,55]))
