"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=0, hours=0, hourly_wage=0, contracts=0, commission_per_contract=0, bonus_commission=0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.hourly_wage = hourly_wage
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract
        self.bonus_commission = bonus_commission

    def get_pay(self):
        """Return the pay for this employee in dollars."""
        if self.salary > 0:
            pay = self.salary
        else:
            pay = self.hours * self.hourly_wage

        if self.contracts > 0:
            pay += self.contracts * self.commission_per_contract
        else:
            pay += self.bonus_commission

        return pay

    def __str__(self):
        """Return a string describing this employee."""
        if self.salary > 0:
            if self.contracts > 0:
                return f'{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}.'
            elif self.bonus_commission > 0:
                return f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}.'
            else:
                return f'{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}.'
        else:
            if self.contracts > 0:
                return f'{self.name} works on a contract of {self.hours} hours at {self.hourly_wage}/hour and receives a commission for {self.contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}.'
            # elif self.bonus_commission > 0:
            #     return f'{self.name} works on a contract of {self.hours} hours at {self.hourly_wage}/hour and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}.'
            else:
                return f'{self.name} works on a contract of {self.hours} hours at {self.hourly_wage}/hour. Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours=100, hourly_wage=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, contracts=4, commission_per_contract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, hourly_wage=25, contracts=3, commission_per_contract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus_commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, hourly_wage=30, bonus_commission=600)
