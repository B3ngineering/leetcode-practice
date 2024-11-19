class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashmap = {}

        for val in arr:
            if val in hashmap.keys():
                hashmap[val] += 1
            else:
                hashmap[val] = 1
        
        comp_list = list(hashmap.values())
        comp_set = set(comp_list)
        
        return len(comp_list) == len(comp_set)