class Solution:
    def maxFrequencyElement(self, nums) -> int:
        count={}
        max_freqency=0
        max_frequency_element_count=0
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            if max_freqency == count[i]:
                max_frequency_element_count+=1
            if max_freqency < count[i]:
                max_freqency=count[i]
                max_frequency_element_count=1
        return max_frequency_element_count*max_freqency 