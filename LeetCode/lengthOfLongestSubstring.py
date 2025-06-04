def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
              char_set.remove(s[left])
              left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len 

/*
  Implementation is in Sliding Window technique. Size of the largest window / set is returned with no repeating elements
  The Space Complexity of this algorithm is O(n).
  The Time Complexity of this Algorithm is O(n).

  The key when solving repeating elements type problems is to use Sets. Sets do not allow for repeating characters and have constant access time, which make them ideal for such problems.
*/
