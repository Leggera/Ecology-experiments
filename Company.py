import random
class Company:
    def __init__(self, name, location, size, taxes, allowed_pollution):
        self.name = name 
        self.location = location
        self.size = size
        self.taxes = taxes
        self.allowed_pollution = allowed_pollution
        self.made_pollution = 0
        self.is_working = True
        self.filters = 0
    def stop_working(self):
        self.is_working = False
    def resume_working(self):
        self.is_working = True
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
