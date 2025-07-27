from typing import Optional


from Leetcode.LinkedListGenerator.LinkedListGenerator import generateLinkedListFromArray


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visited = []
        while curr:
            if curr not in visited:
                visited.append(curr)
            else:
                return True
            curr = curr.next
        return len(visited) != len(set(visited))

solution = Solution()
print(solution.hasCycle())
