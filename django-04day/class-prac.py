class human:
    def __init__(self,gender,name,age,character):
        self.gender = gender
        self.name = name
        self.age =age
        self.character = character
        self.get_married = False
        self.has_children = []
        self.status = 'Good'
    def get_bad(self):
        self.character = 'Fighter'
    
    def hit_someone(self,chip):
        chip.status = 'Wound'
    
    def __str__(self):
        return '\n이름 : %s \n성별 : %s \n나이 : %s \n성격 : %s \n결혼여부 : %s \n자녀들 : %s \n상태 : %s' % (self.name, self.gender, self.age, self.character, self.get_married, self.has_children, self.status)

# 일반 함수 정의
def get_marriage(chip1, chip2):      # 다람쥐 둘이 결혼을 하면
    chip1.get_married = True         # 각 다람쥐들의 결혼여부가 참이 됨
    chip2.get_married = True
    chip1.has_children = ['Noah', 'Sion', 'John']
    chip2.has_children = ['Noah', 'Sion', 'John']


# 코드 시작

Kevin = human(name='Kevin', gender='male', age=30, character='순함')      # 다람쥐 객체 톨과 Alice 정의
Alice = human(name='Alice', gender='female', age=28, character='깍쟁이')
print(Kevin)               # Kevin의 상태 출력
Alice.hit_someone(Kevin)    # Alice가 Kevin을 때리는 매소드 실행
print(Kevin)               # Kevin의 상태 다시 출력
Alice.get_bad()  # 겨울이 왔을 때 Alice의 성격 변화
get_marriage(Kevin, Alice)   # Kevin과 Alice가 결혼하는 함수 실행
print(Alice)             # Alice의 상태 출력