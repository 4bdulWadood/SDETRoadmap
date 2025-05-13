class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        '''
            Maximum Number of Words Found in Sentences - LeetCode #2114

            Problem :
            A sentence is a list of words that are separated by a single space with no leading or trailing spaces. You are given a list of strings sentences, where each sentences[i] represents a single sentence. 
            Return the maximum number of words that appear in a single sentence.

        
        '''

        return sorted(s) == sorted(t)


