#       TITLE: Fruit Into Baskets
#  DIFFICULTY: Medium
# DESCRIPTION: You are visiting a farm that has a single row of fruit trees arranged from left to right. 
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
#   - You only have two baskets, and each basket can only hold a single type of fruit.
#     There is no limit on the amount of fruit each basket can hold.
#   - Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. 
#     The picked fruits must fit in one of your baskets.
#   - Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

# Algorithm details:
# see code comments

class Solution(object):
    from collections import deque
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        len_fruits = len(fruits)                # length of fruits array
        fruit_counts = Counter()                # counter dict to keep track of fruits seen
        distinct = 0                            # number of distinct fruits
        max_fruits = 2                          # max number of distinct fruits allowed
        result = 0                              # store result
        start = end = 0                         # sliding window start/end
        
        while end < len_fruits:
            if fruit_counts[fruits[end]] == 0:             # if the current fruit hasn't been seen
                distinct += 1                              # update our distinct count (max is 2)
            fruit_counts[fruits[end]] += 1                    # update fruit counter
             
            while distinct > max_fruits:                # if too many distinct fruits, shrink window
                fruit_counts[fruits[start]] -= 1        # decrement the start
                if fruit_counts[fruits[start]] == 0:    # if start no longer included in window
                    distinct -= 1                           # decrease distinct count
                start += 1                              # increment the start
                
            result = max(result, end-start+1)           # get results using max of previous vs now
            end += 1                                    # increment the end
            
        return result
