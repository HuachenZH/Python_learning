class Solution:
    def minimumSum(self, num: int) -> int:
        # get the four digits
        digit1=num%10
        digit2=int(num%100/10) # int() can round down
        digit3=int(num%1000/100)
        digit4=int(num%10000/1000)
        
        # combination
        # as the expected output is only the min sum, no need to get all the combinations. Only get the pair which can give the min sum

        # put the four digits in a list and sort them
        digitList= [digit1, digit2, digit3, digit4]
        digitList.sort()

        # the two smallest digits will be on the ten's digit and unit's digit



        return digitList



sol=Solution()
print(sol.minimumSum(2987))
