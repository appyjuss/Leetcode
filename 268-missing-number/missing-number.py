'''
input: array of int
the int will be in the range lenght of the array

[0,1,2,4] > 4
[0,1,2,3,4] -> 5

output - > 3

edge cases:
[0], [1] ->  1, 0

plan:
from  to len(arr)

[0,1,2,3] -> 4


'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums) + 1):
            if i not in nums:
                return i
            