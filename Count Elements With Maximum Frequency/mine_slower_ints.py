class Solution:
    def maxFrequencyElement(self, nums) -> int:
        count={}
        max_freqency=0
        max_frequency_element_count=0
        for i in nums:
            count[i] = count.get(i, 0) + 1
            if max_freqency == count[i]:
                max_frequency_element_count+=1
            if max_freqency < count[i]:
                max_freqency=count[i]
                max_frequency_element_count=1
        return max_frequency_element_count*max_freqency

if __name__ == "__main__":
    a =Solution()
    print(a.maxFrequencyElement([1,2,2,3,1,4]))