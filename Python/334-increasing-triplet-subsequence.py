class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = float('inf')
        b = float('inf')

        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False
        # We move through the array, and track the minimum and the smallest value to its right.
        # Then, if we see a value that is greater after that, we return true