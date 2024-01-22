class Solution(object):
    def getMaximumGenerated(self, n):
        nums = [0 for _ in range(205)]
        nums[0] = 0
        nums[1] = 1
        for i in range(1, n):
            nums[2 * i] = nums[i]
            nums[2 * i + 1] = nums[i] + nums[i + 1]
        
        return max(nums)