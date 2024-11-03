class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # Simple solution with
        merged_string = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                merged_string.append(word1[i])
            if i < len(word2): 
                merged_string.append(word2[i])
        
        return ''.join(merged_string)