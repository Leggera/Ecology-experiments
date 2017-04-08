import random
class Company:
    def __init__(self, name, location, size, taxes, allowed_pollution):
        self.name = name 
        self.location = location
        self.size = size
        self.taxes = taxes
        self.allowed_pollution = allowed_pollution
        self.made_pollution = 0.0
        self.daily_pollution = 0.0
        self.is_working = True
        self.filters = 0
        self.day_count = 0
        self.install_filter = False
    def stop_working(self):
        self.is_working = False
    def resume_working(self):
        self.is_working = True
    def pollute(self):
        if (self.is_working):
            pollution = float(random.randint(3, 10))#TODO
            if (self.filters > 0):
                pollution -= 0.07 * self.filters * pollution
            self.made_pollution += pollution
            print self.made_pollution
            self.daily_pollution = pollution
            #Town.add_pollution(pollution)?
            return pollution
        return 0
    def add_filter(self):
        self.install_filter = True
    def manage(self):
        if (self.install_filter):
            if (self.day_count < 7):
                self.day_count += 1
            else:
                self.filters += 1
                self.day_count = 0
                self.install_filter = False
