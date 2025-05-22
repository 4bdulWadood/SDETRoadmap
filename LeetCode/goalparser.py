class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        
        '''
            You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()", and/or "(al)" in some order. The Goal Parser will interpret "G" as the strnig "G", "()", as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

            Given the string command, return the Goal Parser's interpretation of command.

            command.replace("()", "o").replace("(al), "al")

            Time Complexity : O(n)
            * Each .replace() call must scan the entire string, so if the length of command is n, each .replace() takes O(n) time. overall time complexity is O(n).

            Space Complexity : 
            * .replace() in Python returns a new string - strings are immutable in Python, so each .replace() creates a copy. meaning Space Complexity is O(2n)

            the .replace function might come in handy, it returns a mutated version of the string, takes in two parameters, the character/s to replace and the character to be replaced.
        ''' 

        return command.replace("()", "o").replace("(al)", "al")
