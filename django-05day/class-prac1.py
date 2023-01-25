class person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        self.state = 'Normal'
        self.married = False
        self.children = []
    
    def hitted(self,hit):
        hit.state = "Bitten"
        
    def __str__(self) -> str:
        return '\nname: %s \nage: %d \nstate: %s \nmarried: %s \nChildren: %s' % (self.name,self.age,self.state,self.married,self.children)

def married(arg1,arg2):
    arg1.married = True
    arg2.married = True
    arg1.children = ['Zion','Noah']
    arg2.children = ['Zion','Noah']

   
a = person('Kevin',30,)
b = person('Alice',28)
print(a,"\n",b)
b.hitted(a)
married(a,b)
print(a,"\n",b)