class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Harry", 1200000, 211019)
print(p.name, p.salary, p.pincode, p.company)
r = Programmer("Parth", 1100000, 289078)
print(r.name, r.salary, r.pincode, r.company)
 