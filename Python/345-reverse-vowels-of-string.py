class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Identify the vowels
        # Map to track each vowels index
        # For loop to get vowels and indices, then another loop to reverse them
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        length = len(s)
        dictionary = []

        for i in s:
            if i in vowels:
                dictionary.append(i)      

        s = list(s)
        i = len(dictionary)

        for j in range(length):
            if s[j] in vowels:
                i -= 1
                s[j] = dictionary[i]
                        
        return ''.join(s)