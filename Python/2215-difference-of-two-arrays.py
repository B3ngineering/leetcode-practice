class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        answer = []

        if len(nums1) == 0:
            return nums2
        if len(nums2) == 0:
            return nums1

        set1 = set(nums1)
        set2 = set(nums2)

        answer.append(list(set1.difference(set2)))
        answer.append(list(set2.difference(set1)))

        return answer
        
        # For each element in 1, if not in 2, answer[1].append(element)        