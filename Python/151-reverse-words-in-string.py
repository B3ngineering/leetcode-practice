class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Should be easy enough to loop over in reverse and add to a new string
        # Strings are immutable - we can use an array and convert to string
        # Remove trailing and leading spaces
        s.strip()
        current_word = []
        current_string = []
        length = len(s)
        i = 0

        for char in s:
            i += 1
            if char != " ":
                current_word.append(char)
            elif len(current_word) > 0:
                current_string.append("".join(current_word))
                current_word = []
            if i == length:
                current_string.append("".join(current_word))

        current_string.reverse()
        print(current_string)
        return " ".join(current_string).strip()

        # This solution works - but we can also just use .strip(), .split(), .reverse() - extra Python syntax knowledge would be required