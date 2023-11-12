class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        m=0
        f=lambda : (m*10)+(n%10)
        while n > 0:
            n,m=n//10,f()
            
        return m==x
