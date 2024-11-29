class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        # Automatically return false if the words are not of equal length
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        # Convert to lists for easier parsing
        chars = set(word1)
        word1_map = {}
        word2_map = {}

        # Fill the map with characters / counts
        for char in chars:
            word1_map[char] = word1.count(char)
            word2_map[char] = word2.count(char)

        # If the counts are different, return false
        if sorted(word2_map.values()) != sorted(word1_map.values()):
            return False
        
        return True