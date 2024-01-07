class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) 
        if n < 3:
          return False

        i = float('inf')
        j = float('inf')
        for num in nums:
           if num <=i:
              i = num
           elif num <= j:
              j = num
           else:
              return True
        return False
              


print(Solution().increasingTriplet([20,100,10,12,5,13]))