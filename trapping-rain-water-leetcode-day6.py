class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height) - 1
        final=0
        l = height[left]
        r = height[right]
        while left < right:
            if l< r:
                left += 1
                if l < height[left]:
                    l = height[left]
                else:
                    final += l - height[left]
            else:
                right -= 1
                if r < height[right]:
                    r = height[right]
                else:
                    final += r - height[right]
        return final
