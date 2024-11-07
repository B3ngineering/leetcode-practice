class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = sum(nums[:k])
        max_sum = current_sum 
        
        for left in range(1, len(nums) - k + 1):
            current_sum = current_sum - nums[left - 1] + nums[left + k - 1]
            max_sum = max(max_sum, current_sum)
        
        max_avg = max_sum / float(k)
        
        return max_avg
