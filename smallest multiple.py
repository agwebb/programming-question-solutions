import time
class hopes_and_prayers:
    def __init__(self, limiter):
        self.limiter = limiter

    def logic(self):
        checked = self.limiter
        print(self.limiter)
        while True:
            if all(checked % i == 0 for i in range(1, self.limiter + 1)):
                return checked
            print(checked, "\n")
            #checked += indexer
            checked+= self.limiter
            #hi
instance1 = hopes_and_prayers(20)

print("result: ", instance1.logic())
