# paths:
    # get the four digits
    # combination
    # find the minimum


class Solution:
    def minimumSum(self, num: int) -> int:
        # get the four digits
        digit1=num%10
        digit2=int(num%100/10) # int() can round down
        digit3=int(num%1000/100)
        digit4=int(num%10000/1000)
        
        # combination
        return [digit1, digit2, digit3, digit4]
    


sol=Solution()
sol.minimumSum(2887)
