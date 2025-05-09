class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) == 1:
            return False

        for index, item in enumerate(s):
            if item in "({[":
                stack.append(item)
            elif item in ")}]": 
                if not stack:
                    return False
                if (
                    (stack[-1] == "(" and item == ")")
                    or (stack[-1] == "{" and item == "}")
                    or (stack[-1] == "[" and item == "]")
                ):
                    stack.pop()
                else:
                    return False;

        return not stack

#Beats 100% in Runtime and 56.91% in Memory 
#Time Complexity : O(n)
#Space Complexity : O(n) (worst case)
'''
        An input string is valid if :
        1. Open Brackets : Must be closed by the same type of brackets.
        2. Open Brackets : must be closed in the correct order.
        3. Every closed bracket has a corresponding open bracket of the same type.

        Solution Strategy :
        A stack data structure can be employed to solve the problem.
        When you have "(", "{" "[" Push to Stack. (LIFO Stack).

        At the top of the Stack make sure you have corresponding ")","}","]", during removal of corresponding paranethesis, if you don't have corresponoding ")", "}" or "]" then return False. 

        Beats 100% in Runtime and 56.91% in Memory !
        Time Complexity : O(n)
        Space Complexity : O(n) (worst case)
'''
