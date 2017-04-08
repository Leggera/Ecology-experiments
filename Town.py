import numpy as np
class Town:
    def __init__(self, Fund, filter_cost, fee, critical_pollution, Companies, Area, Cars):
        self.Fund = Fund
        self.Companies = Companies
        self.Area = Area
        self.Cars = Cars
        self.Pollution = np.array([0.0, 0.0, 0.0])
        self.residual_pollution = 0
        self.points= [(25, 25), (20, 80), (50, 20)]#TODO
        self.filter_cost = filter_cost
        self.fee = fee
        self.critical_pollution = critical_pollution    

    def add_money_to_fund(self, money):
        self.Fund += money
    def get_money_from_fund(self, money):
        if (self.Fund >= money):
            self.Fund -= money
            return True
        else:
            return False
    def penalty_company(self, company):
        if  (company.daily_pollution > company.allowed_pollution):
            if (company.daily_pollution > self.critical_pollution):
                company.stop_working()
                print "Stop working"
            else:
                self.add_money_to_fund(self.fee)
    def reduce_cars(self, amount):
        self.Cars.percent *= amount
    def measure_pollution(self):
        return self.Pollution
    def add_pollution(self, pollution, location = None):
        if (location is not None):
            x, y = location
            count = 0
            for point in self.points:
                c1, c2 = point
                self.Pollution[count]+=float(pollution)/((x-c1)*(x-c1) + (y-c2)*(y-c2))
                count += 1
        else:
            self.Pollution+=pollution
            self.residual_pollution += pollution
    def reduce_pollution(self, pollution):
        self.Pollution-=pollution
        for i, pol in enumerate(self.Pollution):
            if (pol < 0):
                self.Pollution[i] = 0
        self.residual_pollution -= pollution
        if (self.residual_pollution < 0):
            self.residual_pollution = 0
