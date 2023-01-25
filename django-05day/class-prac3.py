class Human:
    def __init__(self,gender,name,age) -> None:
        self.gender = gender
        self.name = name
        self.age = age
        self.married = False
        self.state = 'Single'
        self.children = []
        self.gethouse = False
           
    def __str__(self) -> str:
        return '\nname: %s \nage: %d \ngender: %s \nmarried: %s \nstate: %s \nChildren: %s \nhouse: %s' % (self.name,self.age,self.gender,self.married,self.state,self.children,self.gethouse)

class Man(Human):
    def say(self):
        self.say = "Korean"
        print(self.say)

def married(a1,a2):
        a1.married = True
        a2.married = True
        a1.state = 'Married'
        a2.state = 'Married'    

def childrn(a1,a2):
    if a1.married == True and a2.married == True:
        a1.children = ['Sion','Noah']
        a2.children = ['Sion','Noah']
        
def gethouse(a1,a2):
    a1.gethouse = "Owned"
    a2.gethouse = "Owned"


kevin = human('Male','Kevin',33)
alice = human('female','Alice',30)

print(kevin)
print(alice)

married(kevin,alice)

print(kevin)
print(alice)

childrn(kevin,alice)
print(kevin)
print(alice)

gethouse(kevin,alice)
print(kevin)
print(alice)

Hellen = man("Female","Hellen",35)
print(Hellen.gender,Hellen.say())