class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp=[]
        dp.append(1)
        result=1
        for i in range(1,n+1):
            if i<=2:
                result=result*9
            else:
                result=result*(10-i+1)
            dp.append(dp[i-1]+result)
            print(result)
        return dp[n]
        