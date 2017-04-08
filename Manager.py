from Town import *
from Company import *
from Cars import *

class Manager:
    def __init__(self, Car_pollution, K, Fund, filter_cost, fee, critical_pollution):
        Companies, Area = self.read_interface()
        Cars_ = Cars(K, Car_pollution)
        self.Town = Town(Fund, filter_cost, fee, critical_pollution, Companies, Area, Cars_)
        self.Weather = 0
        self.smth = dict()
    def read_interface(self):
        Companies = []
        for i, line in enumerate(open("Companies.txt", 'r')):
            if (i == 0):
                Area = tuple(line.rstrip().split(','))
            else:
                name, location, size, taxes, pollution = tuple(line.rstrip().split(','))
                x, y = tuple(location.split())
                Companies += [Company(name, tuple([float(x), float(y)]), float(size), int(taxes), float(pollution))]

        return (Companies, Area)#TODO
    def main(self):
        
        if (self.smth["spec.mode"]):
            self.Town.reduce_cars(float(self.smth["spec.mode"]))
        car_pollution = self.Town.Cars.pollute()
        self.Town.add_pollution(car_pollution)
        
        for company in self.Town.Companies:
            if (int(self.smth[company.name+"stop working"]) >= 1):
                company.stop_working()
            else:
                company.resume_working()
            if (company.is_working):
                self.Town.penalty_company(company)
            if (int(self.smth[company.name+"filters"])>=1):                    
                money = self.Town.filter_cost
                if (self.Town.get_money_from_fund(money)):
                    company.add_filter()
                else:
                    print "no money"
            pollution = company.pollute()
            self.Town.add_pollution(pollution, company.location)
            if (company.is_working):
                self.Town.add_money_to_fund(company.taxes)
            company.manage()
        self.Weather = random.randint(0, 5000)#TODO
        if (self.Weather > 0):
            self.Town.reduce_pollution(self.Weather)
