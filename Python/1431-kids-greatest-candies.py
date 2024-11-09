class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        # Find the current greatest
        # Loop through and add extraCandies
        # If extra candies plus candies[i] > greatest, return_bools[i] = true
        max_candies = max(candies)
        is_greatest = []
        for num in candies:
            if num + extraCandies >= max_candies:
                is_greatest.append(True)
            else:
                is_greatest.append(False)
        return is_greatest
