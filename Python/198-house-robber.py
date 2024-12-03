class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)

        # Handle edge cases
        if length == 1:
            return nums[0]
        
        if length == 2:
            return max(nums[0], nums[1])
        
        prev2 = 0
        prev1 = 0

        for num in nums:

            # Use current and prevs to track the max profit up to each point, and decide to rob or not
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        
        return current
    
# Time complexity: O(n)
# Bottom-up dynamic programming approach