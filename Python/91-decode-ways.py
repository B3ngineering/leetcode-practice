class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Initial naiive approach

        # window = deque()
        # ways = 1

        # # Handle invalid input
        # if s[0] == '0':
        #     return 0

        # for char in s:
        #     window.append(char)
        #     value = int("".join(map(str, window)))
        #     if value < 27:
        #         if len(window) == 2:
        #             ways += 1
        #             window.popleft()
        #         if value == 0:
        #             window.popleft()
        #     else:
        #         window.popleft()
        
        # return ways

        # Handle edge cases
        size = len(s)
        if size == 0 or s[0] == '0':
            return 0
        
        # Create our dp array, and set single digits to 1
        dp = [0] * (size + 1)
        dp[0], dp[1] = 1, 1

        # Iterate over the second to last
        for i in range(2, size + 1):

            # Use fibonacci-like strategy to track number of ways
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[size]
    
# Time complexity: O(n)
# Dynamic programming approach using memoization