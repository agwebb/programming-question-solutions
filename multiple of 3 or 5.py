#our goal is to make a function that solves for the multiples of 3 or 5
#we can make a generator that sums the values up, use a for loop and an
#if assessment statement inside to assess whether or not its correct.
#were going to make this for loop go from 0 to n
#andrew webb

class solvermethod:
    def __init__(self, multiple1, multiple2, towhat):
        self.multiple1 = multiple1
        self.multiple2 = multiple2
        self.limit = towhat
    def solver(self):
        sum = 0
        for values in range(self.limit):
            if values%self.multiple1 == 0 or values%self.multiple2 == 0:
                sum += values
        return sum

value1 = 3
value2 = 5
limit1 = 1000
valueneeded = solvermethod(value1, value2, limit1)
result = valueneeded.solver()
print(result)