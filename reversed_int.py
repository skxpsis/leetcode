# REVERSED 32 BIT INT - EASY
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        upper_bound = 2**31-1
        lower_bound = -2**31
        
        # must say within 32 bits; 64 not accepted
        if (x >= upper_bound) or (x <= lower_bound):
            return 0
        else:
            # convert int to str for iteration
            x_str = str(x)
            # if x>0, just reverse it
            if x >= 0:
                x_reversed = x_str[::-1]
            # if x<0, need to remove the negative sign then reverse
            # add negative sign back in at end
            else:
                # holds all values of x except for first value (the negative sign)
                temp = x_str[1:]
                # writes temp backward
                temp2 = temp[::-1]
                # concatenate negative sign and temp2 value for new number
                x_reversed = "-" + temp2
        # return type should be int for x reversed
        x_reversed = int(x_reversed)
        if (x_reversed >= upper_bound) or (x_reversed <= lower_bound):
            return 0
        else:
            return x_reversed
        