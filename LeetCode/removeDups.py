
class Solution(object):
    def removeDups(head):
        seen = set()
        current = head
        prev = None
        while current:
            if current.val in seen:
                prev.next = current.next
            else:
                seen.add(current.val)
                prev = current
            current = current.next


```
  Time Complexity: O(n)
  Space Complexity: O(n)
  Difficulty: 🟡 Medium
```
class Solution(object):
    def removeDups(head):
        current = head
        while current:
            runner = current
            while runner.next:
                if runner.next.val == current.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
      
```
  Time Complexity: O(n²)
  Space Complexity: O(1)
  Difficulty: 🔴 Hard
```
