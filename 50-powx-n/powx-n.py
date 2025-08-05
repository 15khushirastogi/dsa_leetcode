class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
      
        binform=n
        if n<0:
            x=1/x
            binform=-binform

        ans=1
        while binform>0:
            if binform%2==1:
                ans*=x
            x*=x
            binform//=2

        return ans
