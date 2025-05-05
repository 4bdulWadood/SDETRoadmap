class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        for index, char in enumerate(string):  # Correct order: index first, then char
            if index >= len(string) - index - 1:  # Stop when reaching the middle
                return True
            if char != string[len(string) - index - 1]:
                return False
        return True  # For empty string case (though x can't be empty)

        # You loop through half the strings n/2 comparisons, but in Big O notation we simplify to O(n)
        # Space Complexity : O(n) : Converting X to A string requires O(n) extra space!.
