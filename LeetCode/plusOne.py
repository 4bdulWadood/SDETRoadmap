class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        num = int(''.join(map(str, digits)))
        num = num + 1
        return list(map(int, str(num)))
        
        ''.join(map(str, digits)))
