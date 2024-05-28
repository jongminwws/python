#human 클래스를 선언
class human:
    def __init__(self,name,age,gender): #기본 생성자, 매개변수 3개인 생성자 (이때 self는 생략 불가능)
        self.name= name
        self.age = age
        self.gender = gender
        
    def who(self): # 클래스 안에 함수(def) : 메서드
        print(self.name)
        print(self.age)
        print(self.gender)
#human 클래스를 인스턴스화 해서 객체 생성
# areum = human() # 기본 생성자 호출
areum = human("이름",25,"남성") # 매개변수 3개인 생성자 호출

#인스턴스 속성에 접근
print(areum.age)

# 인스턴스 메서드에 접근
print.who()