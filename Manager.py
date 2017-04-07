from Town import *
from Company import *
from Cars import *

class Manager:
    def __init__(self, N, K, Fund):
        Companies, Area, Car_pollution = self.read_interface()
        Cars_ = Cars(K, Car_pollution)
        self.Town = Town(Fund, Companies, Area, Cars_)
        self.Weather = 0
    def read_interface(self):
        Companies = []
        for line in open("Companies.txt", 'r'):
            location, size, taxes, pollution = tuple(line.rstrip().split(','))
            x, y = tuple(location.split())
            Companies += [Company(tuple([float(x), float(y)]), float(size), int(taxes), float(pollution))]
        #Companies = [Company(i, 100, 200) for i in range(5)]
        return (Companies, 20, 0.8)#TODO
    def main(self):
        
        #print self.N
        #for i in range (25):
        self.Town.add_car_pollution()
        self.Town.reduce_cars(2)
        print self.Town.measure_pollution()
        for company in self.Town.Companies:
            pollution = company.pollute()
            self.Town.add_pollution(pollution) #TODO
            if (company.is_working):
                self.Town.penalty_company(company)
            if (random.randint(0, 1)):                    
                money = 200
                if (self.Town.get_money_from_fund(money)):
                    company.add_filter()
                    print "add filter"
            if (company.is_working):
                self.Town.add_money_to_fund(company.taxes)
            #company.reset_pollution()#TODO why?
        self.Weather = random.randint(0, 2000)
        if (self.Weather > 0):
            self.Town.reduce_pollution(self.Weather)
