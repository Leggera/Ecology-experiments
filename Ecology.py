import random
class Town:
    def __init__(self, Fund, Companies, Area, Cars):
        self.Fund = Fund
        self.Companies = Companies
        self.Area = Area
        self.Cars = Cars
        self.Pollution = 0
        
    
    def add_car_pollution(self):#OK
        self.Pollution += self.Cars.percent * (self.Cars.amount_()) * (self.Cars.pollution_())
    def add_money_to_fund(self, money):#OK
        self.Fund += money
    def get_money_from_fund(self, money):#OK
        if (self.Fund >= money):
            self.Fund -= money
            return True
        else:
            return False
    def penalty_company(self, company):
        some_amount = 100
        if  (company.made_pollution > company.allowed_pollution):
            if (company.made_pollution > some_amount):
                company.stop_working()
            else:
                add_money_to_fund(money)
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

class Company:
    def __init__(self, location, taxes, allowed_pollution): 
        self.location = location
        self.taxes = taxes
        self.allowed_pollution = allowed_pollution
        self.made_pollution = 0
        self.is_working = True
        self.filters = 0
    def stop_working(self):
        self.is_working = False
    def pollute(self):
        if (self.is_working):
            pollution = random.randint(1, 5)
            if (self.filters > 0):
                pollution /= self.filters
            self.made_pollution += pollution
            #Town.add_pollution(pollution)?
            return pollution
        return 0
    def reset_pollution(self):
        self.made_pollution = 0
    def add_filter(self):
        self.filters += 1

class Cars:
    def __init__(self, amount, pollution):
        self.amount = amount
        self.pollution = pollution
        self.percent = 0.5
    def amount_(self):
        return self.amount
    def pollution_(self):
        return self.pollution

class Manager:
    def __init__(self):
        N, K, Fund, Companies, Area, Car_pollution = self.read_interface()
        self.N = N
        self.K = K
        Cars_ = Cars(K, Car_pollution)
        self.Town = Town(Fund, Companies, Area, Cars_)
        self.Weather = 0
    def read_interface(self):
        Companies = [Company(i, 100, 200) for i in range(5)]
        return (5, 10, 100, Companies, 20, 0.8)
    def update_interface(self):
        return
    def main(self):
        for i in range (25):
            self.Town.add_car_pollution()
            self.Town.reduce_cars(2)
            print self.Town.measure_pollution()
            for company in self.Town.Companies:
                pollution = company.pollute()
                self.Town.add_pollution(pollution)
                self.Town.penalty_company(company)
                if (random.randint(0, 1)):                    
                    money = 50
                    if (self.Town.get_money_from_fund(money)):
                        company.add_filter()
                        print "add filter"
                if (company.is_working):
                    self.Town.add_money_to_fund(company.taxes)
                company.reset_pollution()
            self.Weather = random.randint(0, 5)
            if (self.Weather > 0):
                self.Town.reduce_pollution(self.Weather)
            self.update_interface()
if __name__ == "__main__":
    
    manager = Manager()
    manager.main()
