# TITLE:        Reversed Integer
# DESCRIPTION:  Given a signed 32-bit integer x, return x with its digits reversed.
#               If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#               Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# DIFFICULTY:   Medium

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        upper_bound = 2**31-1                                    # accounting for 32-bit int range
        lower_bound = -2**31
        
        if (x >= upper_bound) or (x <= lower_bound):             # must say within 32 bits; 64 not accepted
            return 0
        else:
            x_str = str(x)                                       # convert int to str for iteration
            if x >= 0:                                           # if x>0, just reverse it
                x_reversed = x_str[::-1]
                                                                 # if x<0, need to remove the negative sign then reverse
                                                                 # add negative sign back in at end
            else:
                temp = x_str[1:]                                 # holds all values of x except for first value (the negative sign)
                temp2 = temp[::-1]                               # writes temp backward
                x_reversed = "-" + temp2                         # concatenate negative sign and temp2 value for new number
        x_reversed = int(x_reversed)                             # return type should be int for x reversed
        
        if (x_reversed >= upper_bound) or (x_reversed <= lower_bound):
            return 0
        else:
            return x_reversed
        
