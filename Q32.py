class Bonus:
    def __init__(self,id,amount):
        self.id = id
        self.amount = amount

    def bonus(self):
        return self.amount*0.05
    
    class PremiumBonus:
        def __init__(self,id,amount):
            self.id = id
            self.amount = amount
        
       