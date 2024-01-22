class Solution(object):
    def isPalindrome(self, head):
        given = ''
        while head is not None:
            given += str(head.val)
            head = head.next

        left = 0
        right = len(given)-1
        while left <= right:
            if given[left] != given[right]:
                return False
            left += 1
            right -= 1
        
        return True