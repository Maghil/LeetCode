class Solution:
    def maxFrequencyElements(self, nums) -> int:
        count={}
        max_freqency=0
        max_frequency_elements=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            if max_freqency == count[i]:
                max_frequency_elements.append(i)
            if max_freqency < count[i]:
                max_freqency=count[i]
                max_frequency_elements=[i]
        return len(max_frequency_elements)*max_freqency