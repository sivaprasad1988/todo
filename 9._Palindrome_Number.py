class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        length = len(x) -1
        index = 0
        isCorrect = False
        while length >= 0:
            if x[index] == x[length]:
                isCorrect = True
            else:
                isCorrect = False
                break

            length -= 1
            index += 1
        return isCorrect




solution = Solution()
nums = 121
print(solution.isPalindrome(100))