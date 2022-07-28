#       TITLE: ZigZag Conversion
# DESCRIPTION: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
#              (you may want to display this pattern in a fixed font for better legibility)=
#               P   A   H   N
#               A P L S I I G
#               Y   I   R
#               And then read line by line: "PAHNAPLSIIGYIR"
#               
#               Write the code that will take a string and make this conversion given a number of rows: string convert(string s, int numRows);
#  DIFFICULTY: Medium
#        TIME: O(N)
# 
# Algorithm details:
#   For special cases when the number of rows are 0 or 1, just return s
#   Variable descriptions:
#       - row: this keeps track of what row the current character is being appending to, starting at row 1 up to numRows
#       - direction: designates if we are zig-zagging up or down
#                    up direction implies we are append to row 1, row2, ..., numRows
#                    down direction implies we are appending from numRows, numRows-1, numRows-2, ..., row 1
#                    row is defined by the direction at each stage of the for loop
#                    so when direction is negative, we decrease in row each time until the first row is reached (numRows == 1)
#                    when it's positive, it increases until the last row is reached (numRows)
#       - lines: dictionary where the rows are stored
#                keys correspond to the row number (1, 2, ..., numRows)
#                values correspond to the chars appending to that row
#   Iterate through each char in the input string
#     If the current row is not yet in the lines dict, add it
#     Else, appending the current char in the input string to the current row's value
#     Increment (if direction == 1) or decrement (if direction == -1) the row by the current direction
#      If the current row is the first row (row 1) or the last row (numRows)
#         Change the direction of rows by multiplying it by -1
#           If the direction is positive (direction == 1), it will turn negative (1 * -1 = -1)
#           If the direction is negative (direction == -1), it will become positive (-1 * -1 = 1)
#      Repeat until all chars have been visited
#    Join all values present in the dict and return it
                    
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2: 
            return s
        
        row = 1                                 # row index
        direction = 1                           # direction == 1 if going down, == -1 if going up
        lines = {}                              # lines stored in dict
        
        for char in s:                          # loop through input string
            if row not in lines:                # if row not in dict
                lines[row] = char                 # add it to the dict
            else:
                lines[row] += char              # else for that row, append the current char to it
            row += direction                    # increase or decrease the row according to the step
            if row == 1 or row == numRows:      # if at beginning or end of of s, switch direction
                direction *= -1                   # decrement to go change direction to up or down
                
        ans = ''.join(lines.values())           # join all values of dict together
        return ans
      
