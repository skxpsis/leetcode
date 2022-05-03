# IS PALINDROME - EASY
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            num_map = list(map(int, str(x)))
            num_map2 = num_map[::-1]
            if num_map == num_map2:
                return True
            else:
                return False
