#       TITLE: Longest Common Prefix
#  DIFFICULTY: Easy
# DESCRIPTION: Write a function to find the longest common prefix string amongst an array of strings.
#              If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = ""
        
        if len(strs) == 0:
            return lcp
        
        for i in range(len(min(strs))):
            char = strs[0][i]
            if all(a[i]==char for a in strs):
                lcp += char
            else:
                break
        return lcp
                
