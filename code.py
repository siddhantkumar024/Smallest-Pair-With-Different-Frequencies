class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        nums.sort()
        d={}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        g=[]
        f=d[nums[0]]
        g.append(nums[0])
        i=False
        for k,v in d.items():
            if v!=f:
                i=True
                g.append(k)
                break
        
        if i:
            return g
        else:
            return [-1,-1]
        

        
