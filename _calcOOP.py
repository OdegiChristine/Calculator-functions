# ODEGI CHRISTINE AWUOR
# SCT211-0093/2022

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        total = self.num1 +self.num2
        print(f"Sum = {total}")
        return total

    def subtraction(self):
        difference = self.num1 - self.num2
        print(f"Difference = {difference}")
        return difference

added = Calculator(19, 38)
added.sum()
added.subtraction()
