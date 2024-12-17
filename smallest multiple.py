class hopes_and_prayers:
    def __init__(self, limiter):
        self.limiter = limiter

    def logic(self):
        checked = 1
        while True:
            if all(checked % i == 0 for i in range(1, self.limiter + 1)):
                return checked
            checked += 1

instance1 = hopes_and_prayers(20)

print(instance1.logic())
