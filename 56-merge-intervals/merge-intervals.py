class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        st=intervals[0][0]
        en=intervals[0][1]
        l=[]
        for i in range(len(intervals)-1):
            if(en>=intervals[i+1][0]):
                en=max((intervals[i][1]),(intervals[i+1][1]),en)
            else:
                x=[st,en]
                l.append(x)
                st=(intervals[i+1][0])
                en=(intervals[i+1][1])
        x=[st,en]
        l.append(x)
        return l

