
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #In this problem a basic implementation of the frequency counter should suffice.
        # Given an array ums of size n, return the majority element.
        # The majority element is the element that appears more than n / 2 times. You may assume that the majority elemet always exists in the array.

        # Time Complexity : O(n)
        # You iterate through the list once to count the frequencies.
        # Each insertion / update operation in the hash map (dictionaty) is O(1) on average.
        # So total time: O(n) where n is the number of elements in the list.

        # Space Complexity : O(n)
        # In the worst case, all elements in the list are unique
        # That means the hash map will store n key-value pairs (one for each unique element)
        # So space used by the hash map is O(n)

        freq_counter = Counter(nums)


        n = len(nums)
        threshold = n / 2

        #Iterate over the frequency counter and check for the majority element
        for num, count in freq_counter.items():
            if count > threshold:
                return num
        
        return None
    
