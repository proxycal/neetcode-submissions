class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestlength=0 
        nums_set=set(nums) 
        for i in nums_set:
            count=1
            if i-1 not in nums_set:
                while i+1 in nums_set:
                    i=i+1
                    count+=1
                if count > longestlength:
                     longestlength=count
        return longestlength



        