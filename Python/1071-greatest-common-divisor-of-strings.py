class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Turns out we can almost treat this numerically by first checking if
        # the two strings will in fact be divisible by the same number

        # Then we just need to find the gcd (x) of the string lengths, and the first
        # x characters will be the gcd. 

        if str1 + str2 != str2 + str1:
            return ""

        x = gcd(len(str1), len(str2))
    
        return str1[:x]

def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
        