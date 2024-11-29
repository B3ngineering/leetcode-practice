class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Handle empty case
        if len(nums) == 0:
            return 0

        # Convert to a sorted unique list
        nums = list(set(nums))
        nums.sort()

        # Declare max counter and current counter
        max_length = 0
        current_length = 0


        for i in range(len(nums)):

            # Use try except to handle the last element
            try:
                if nums[i] + 1 == nums[i+1]:
                    current_length += 1
                else:
                    max_length = max(max_length, current_length + 1)
                    current_length = 0
            except IndexError:
                max_length = max(max_length, current_length + 1)
                current_length = 0
                break
        
        return max_length