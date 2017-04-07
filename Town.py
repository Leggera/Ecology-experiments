class Town:
    def __init__(self, Fund, Companies, Area, Cars):
        self.Fund = Fund
        self.Companies = Companies
        self.Area = Area
        self.Cars = Cars
        self.Pollution = 0
        
    
    def add_car_pollution(self):
        self.Pollution += self.Cars.percent * (self.Cars.amount_()) * (self.Cars.pollution_())
    def add_money_to_fund(self, money):
        self.Fund += money
    def get_money_from_fund(self, money):
        if (self.Fund >= money):
            self.Fund -= money
            return True
        else:
            return False
    def penalty_company(self, company):
        some_amount = 100000
        if  (company.made_pollution > company.allowed_pollution):
            if (company.made_pollution > some_amount):
                company.stop_working()
                print "Stop working"
            else:
                self.add_money_to_fund(100)#TODO not taxes
    def reduce_cars(self, amount):
        self.Cars.percent /= amount
    def measure_pollution(self):
        return self.Pollution#???TODO
    def add_pollution(self, pollution):
        self.Pollution+=pollution
    def reduce_pollution(self, pollution):
        self.Pollution-=pollution
        if (self.Pollution < 0):
            self.Pollution = 0