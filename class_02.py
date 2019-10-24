class Calculate_IRRF:
    def __init__(self, salarioBase):
        self.salarioBase = salarioBase
    
    def calculate(self):
        salary = self.salarioBase - (self.salarioBase * 0.11)
        if (salary > 1903.99 and salary < 2826.65):
            discount_INSS = self.salarioBase * 0.11
            discount_IRRF = (self.salarioBase - discount_INSS - 1903.99) * 0.075
            return round(discount_IRRF, 2)
        return self.salarioBase