#       TITLE: Remove K Digits
# DESCRIPTION: Given string num representing a non-negative integer num, and an integer k, 
#              return the smallest possible integer after removing k digits from num.
#  DIFFICULTY: Medium
#        TIME: O(N)
#       SPACE: O(N)
#
# Algorithm details:
  # need to remove as many significant (leftmost) big digits as possible
  # using a monotonic stack
  # when adding a new digit, 
  # we check whether the previous one is bigger than the current and pop it out if so
  # concatenate the remaining elements from the stack as the result

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        answer = ''
        stack = []
        
        for number in num:
            while stack and k > 0 and stack[-1] > number:
                stack.pop()
                k -= 1
            
            if stack or number != '0':
                stack.append(number)
                
        if k > 0:
			      stack = stack[0:-k] 
            
        if stack:
            answer = ''.join(stack)
        else:
            answer = '0'
            
        return answer
        
