class human():
    name = 'Adam'
    age = '6000'
    address = 'Eden'
    wife = True
    def __init__(self,name,age,address,wife):
        self.name = human.name
        self.age = human.age
        self.address = human.address
        self.wife = human.wife
        # print('Created')
    
    def walk(self,name,foot):
        self.foot = foot
        self.name = name
        print(f"{self.name}는 {self.foot}로 걷는다.")
    
    def mouse(self,eat):
        self.eat = eat
        print(f"{self.eat}로 먹는다")

      
A = human('Hwawa',33,'Heaven','Yes')

A.walk('하와','발')
A.mouse('입')