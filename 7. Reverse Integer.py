class Solution:
    def reverse(self, x: int) -> int:
        y=abs(x)
        y=str(y)
        if x<0:
            z="-"+y[::-1]
        else:
            z=y[::-1]
        if -2**31 <= int(z) <= (2**31)-1:
            return int(z)
        else:
            return 0
            
        
