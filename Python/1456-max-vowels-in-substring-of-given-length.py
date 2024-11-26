class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_vowels = 0
        for i in range(len(s)-k+1):
            string = s[i:k]
            current = string.count('a') + string.count('e')+string.count('i')+string.count('o')+string.count('u')
            max_vowels = max(max_vowels, current)
            k += 1

        return max_vowels