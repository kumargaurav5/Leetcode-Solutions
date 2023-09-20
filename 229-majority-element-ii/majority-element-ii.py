class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp={}
        for i in nums:
            if i  not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        l=[]
        n=len(nums)//3
        for i in mp:
            if mp[i]>n:
                l.append(i)
        return l
        