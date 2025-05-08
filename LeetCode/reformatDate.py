class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        
        arr = date.split()
        day = filter(str.isdigit, str(arr[0]))
        if len(day) == 1:
            print(day)
            day = "0" + str(day)

        month_map = {
            "Jan" : "01",
            "Feb" : "02",
            "Mar" : "03",
            "Apr" : "04",
            "May" : "05",
            "Jun" : "06",
            "Jul" : "07",
            "Aug" : "08",
            "Sep" : "09",
            "Oct" : "10",
            "Nov" : "11",
            "Dec" : "12"
        }
        
        month = month_map[arr[1]]

        year = arr[2]

        str1 = "{}-{}-{}".format(year, month, day)
        return str1

'''
  filter() return an iterator, day formatting, string conversion.
  Time Complexity : O(n) where n is the length of the date string, due to the split and filter operations.
  Space Complexity : O(n) for storing the components of the date.
'''
