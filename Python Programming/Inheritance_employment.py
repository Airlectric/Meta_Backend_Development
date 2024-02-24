class Employees:
    def __init__(self,name,last)-> None:
        self.name = name
        self.last = last


class Supervisors(Employees):
    def __init__(self,name,last,password)-> None:
        super().__init__(name,last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return 'Hey i take a leave for ' + str(days) + 'days'

adrian = Supervisors('Adrian', 'A', 'buggy')

emily = Chefs('Emily','E')
janni = Chefs('Janni', 'J')

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)

