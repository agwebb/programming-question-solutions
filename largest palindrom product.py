#Find the largest palindrome made from the product of two
#3 digit numbers.

#method, assess all values from 100 - 999
#since were looking for the largest element we can work our way down from the highest point

class Solution:
    def __init__(self, upperbound, lowerbound):
        self.upperbound = upperbound
        self.lowerbound = lowerbound
    def solver(self):
        highest = 1
        for x in range(self.lowerbound, self.upperbound):
            for y in range(self.lowerbound,self.upperbound):
                valuer = x * y
                strungvaluer = str(valuer)
                if strungvaluer == strungvaluer[::-1] and (valuer >= highest):
                    highest = valuer
        return highest


doer = Solution(1000, 99)
print(doer.solver())