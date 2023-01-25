'''
공대선배 Python coding #9 클래스
'''
# 다람쥐 클래스 정의
class chipmunk:
    def __init__(self, name, gender, age, character): # 생성자: 속성들을 정의
        self.name = name            # 이름
        self.gender = gender        # 성별
        self.age = age              # 나이
        self.character = character  # 성격
        self.is_married = False     # 결혼여부
        self.lst_children = []      # 자녀 리스트
        self.state = '정상'

    def winter_has_come(self):      # 메소드1: 겨울이 오면 성격이 사나워짐
        self.character = "사나움"

    def hit_someone(self, chip):    # 메소드2: 누굴 때리면 걔가 부상을 입음
        chip.state = '부상'

    def __str__(self):
        return '\n이름 : %s \n성별 : %s \n나이 : %s \n성격 : %s \n결혼여부 : %s \n자녀들 : %s \n상태 : %s' % (self.name, self.gender, self.age, self.character, self.is_married, self.lst_children, self.state)

# 일반 함수 정의
def get_marriage(chip1, chip2):      # 다람쥐 둘이 결혼을 하면
    chip1.is_married = True         # 각 다람쥐들의 결혼여부가 참이 됨
    chip2.is_married = True
    chip1.lst_children = ['톨', '담비', '통통']
    chip2.lst_children = ['톨', '담비', '통통']

# 코드 시작

톨 = chipmunk(name='톨', gender='남', age=5, character='순함')      # 다람쥐 객체 톨과 솔모 정의
솔모 = chipmunk(name='솔모', gender='여', age=3, character='깍쟁이')
print(톨)               # 톨의 상태 출력
솔모.hit_someone(톨)    # 솔모가 톨을 때리는 매소드 실행
print(톨)               # 톨의 상태 다시 출력
솔모.winter_has_come()  # 겨울이 왔을 때 솔모의 성격 변화
get_marriage(톨, 솔모)   # 톨과 솔모가 결혼하는 함수 실행
print(솔모)             # 솔모의 상태 출력

출력 = print
출력('한글이름 명령어도 됨')