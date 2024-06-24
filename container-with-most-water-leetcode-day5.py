class Solution(object):
    def maxArea(self, height):
        final = 0
        j = len(height)-1
        i = 0
        while i<j:
            l=j-i
            h=0
            if height[j] > height[i]:
                h=height[i]
                i+=1
            else:
                h=height[j]
                j-=1
            area = l*h
            if area>final:
                final=area
        return final
