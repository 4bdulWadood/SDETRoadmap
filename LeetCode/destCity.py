class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str

        2 Conditions need to be met to return the correct destination city.
        1. City must belong to index 1.
        2. City must not be a starting city.

        Time Complexity : O(n)
        Space Complexity : O(n)

        Beats 100.00% of submissions :) 
        0 ms Runtime.
    


        """
        
        city_dict = {}
        for path in paths:
            if path[1] not in city_dict:
                city_dict[path[1]] = 1
            else:
                city_dict[path[1]] += 1

        # Mark all starting cities with -1
        for path in paths:
            city_dict[path[0]] = -1
        
        for city in city_dict:
            if city_dict[city] == 1:
               return city

