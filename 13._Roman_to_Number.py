class Solution(object):
    def romanToInt(self, s):
        mapping_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        length = len(s) - 1
        total, previous = 0, 0

        while length >= 0:
            number = s[length]
            current_value = mapping_dictionary[number]
            if current_value < previous:
                total -= current_value
            else:
                total += current_value

            previous = current_value
            length -= 1
        return total


solution = Solution()
nums = 'MMMDCCXLIX'
print(solution.romanToInt(nums))
