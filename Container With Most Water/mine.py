class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        i=0
        j=len(height)-1
        width=len(height)-1
        while i<j:
            minimum = min(height[i],height[j])
            area=width*minimum
            max_area=max(max_area,area)
            width=width-1
            if height[i] < height[j]:
                i=i+1
            else:
                j=j-1
        return max_area