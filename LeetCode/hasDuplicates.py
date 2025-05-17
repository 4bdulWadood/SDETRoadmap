def has_duplicates(nums):
    set1 = set()
    for element in nums:
        if element in set1:
            return True
        else:
            set1.add(element)
    return False
