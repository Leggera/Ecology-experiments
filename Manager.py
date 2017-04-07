from Town import *
from Company import *
from Cars import *

class Manager:
    def __init__(self, N, K, Fund):
        Companies, Area, Car_pollution = self.read_interface()
        Cars_ = Cars(K, Car_pollution)
        self.Town = Town(Fund, Companies, Area, Cars_)
        self.Weather = 0
        self.smth = dict()
    def read_interface(self):
        Companies = []
        for line in open("Companies.txt", 'r'):
            name, location, size, taxes, pollution = tuple(line.rstrip().split(','))
            x, y = tuple(location.split())
            Companies += [Company(name, tuple([float(x), float(y)]), float(size), int(taxes), float(pollution))]
        #Companies = [Company(i, 100, 200) for i in range(5)]
        return (Companies, 20, 0.8)#TODO
    def main(self):
        
        #print self.N
        #for i in range (25):
        
        if (self.smth["spec.mode"]):
            self.Town.reduce_cars(float(self.smth["spec.mode"]))
        car_pollution = self.Town.Cars.pollute()
        self.Town.add_pollution(car_pollution)
        print self.Town.measure_pollution()
        for company in self.Town.Companies:
            #print company.name
            #print company.filters
            if (int(self.smth[company.name+"stop working"]) >= 1):
                company.stop_working()
            else:
                company.resume_working()
            if (company.is_working):
                self.Town.penalty_company(company)
            if (int(self.smth[company.name+"filters"])>=1):                    
                money = 250#TODO
                if (self.Town.get_money_from_fund(money)):
                    company.add_filter()
                    #print "add filter"
            pollution = company.pollute()
            self.Town.add_pollution(pollution, company.location) #TODO
            if (company.is_working):
                self.Town.add_money_to_fund(company.taxes)
            company.manage()
            #company.reset_pollution()#TODO why?
        self.Weather = random.randint(0, 5)
        if (self.Weather > 0):
            self.Town.reduce_pollution(self.Weather)
