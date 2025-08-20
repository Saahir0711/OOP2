class Addition:

    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def total(self):
        return self.num1 + self.num2 + self.num3

q1 = Addition(2, 3, 4)
print (q1.total())