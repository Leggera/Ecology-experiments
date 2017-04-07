class Cars:
    def __init__(self, amount, pollution):
        self.amount = amount
        self.pollution = pollution
        self.percent = 0.75
        self.made_pollution = 0
    def amount_(self):
        return self.amount
    def pollution_(self):
        return self.pollution
    def pollute(self):
        pollution = self.percent * self.amount * self.pollution
        self.made_pollution += pollution
        return pollution
