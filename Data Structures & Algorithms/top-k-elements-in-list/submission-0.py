class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        result=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for _ in range(k):
            maxi = 0
            most_frequent = None

            for key in count:
                if count[key] > maxi:
                    maxi = count[key]
                    most_frequent = key

            result.append(most_frequent)
            del count[most_frequent]

        return result



           
              