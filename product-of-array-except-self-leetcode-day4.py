class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        final = [1]*length
        leftCrossProduct = 1
        rightCrossProduct = 1
        for i in range(length):
            final[i] = leftCrossProduct
            leftCrossProduct = leftCrossProduct*nums[i]
        for i in range(length-1,-1,-1):
            final[i] = final[i]*rightCrossProduct
            rightCrossProduct = rightCrossProduct*nums[i]
        return final
