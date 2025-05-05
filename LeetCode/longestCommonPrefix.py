class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:  # Handle empty list
            return ""
        
        prefix = ""
        shortest_str = min(strs, key=len)  # Find the shortest string to avoid IndexError
        
        for num in range(len(shortest_str)):  # Iterate up to shortest string's length
            char = strs[0][num]  # Compare against the first string
            if all(s[num] == char for s in strs):
                prefix += char
            else:
                break

        return prefix

        # Time Complexity O(n*m) and the space complexity is O(p), p is the size of the prefix string created, n is the size of the list, and m is the size of the smallest item in the list.
        # all(char == s[num] for s in strs) is O(1) operation to check a certain index of all items in the list.
