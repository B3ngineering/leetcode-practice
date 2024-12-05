class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dp(left, right, string):

            # When we reach a valid combination, add it to the array and exit the recursion
            if len(string) == n * 2:
                combinations.append(string)
                return

            # If not every left parentheses is present, add one and enter recursion
            if left < n:
                dp(left + 1, right, string + '(')
            
            # If there are less right parentheses than lefts, add right and enter recursion
            if right < left:
                dp(left, right + 1, string + ')')

        combinations = []
        dp(0, 0, '')
        return combinations
        
# Time complexity starts at O(4^n), but gets reduced by if statements avoiding invalid solutions
# Space complexity is O(n)