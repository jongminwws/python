# 내가 만든거
# class Stock:
#     def __init__(self, name, code,per,pbr,배당수익률):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.배당수익률 = 배당수익률
#     def set_name(self, name):
#         self.name = name
#     def set_code(self,code):
#         self.code = code
#     def set_per(self,per):
#         self.per = per
#     def set_pbr(self,pbr):
#         self.pbr = pbr
#     def set_yiled(self,배당수익률):
#         self.배당수익률 = 배당수익률
#     def get_name(self):
#         return self.name
#     def get_code(self):
#         return self.code
#     def get_per(self):
#         return self.per
#     def get_pbr(self):
#         return self.pbr
#     def get_yiled(self):
#         return self.배당수익률
# # 예시를 통해 객체 생성 후 set_name 메서드 사용
# name1 = (input("종목 입력"));
# code1 = int(input("코드입력"));
# per = float(input("per입력"));
# pbr = float(input("pbr입력"));
# yiled = float(input("배당수익률 입력"));
# stock1 = Stock(name1, code1,per,pbr,yiled)

# # get_name과 get_code 메서드를 사용하여 종목명과 종목코드를 얻고 출력
# print("종목명 :" , stock1.get_name())
# print("코드명:" , stock1.get_code())
# print("per :",stock1.get_per())
# print("pbr :",stock1.get_pbr())
# print("배당수익률 :",stock1.get_yiled())

# 강사님이랑 같이 한거
class stock1: # 1. 주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의
    def __init__(self,name,code): # 생성자
        self.name = name
        self.code = code
    # 종목명을 입력할 수 있는 set_name 메서드
    def set_name(self,name):
        self.name = name
    # 종목명을 입력할 수 있는 set_name 메서드
    def set_code(self,code):
        self.code = code
    # 종목명을 리턴하는 get_name 메서드
    def get_name(self):  #
        return self.name
    # 종목코드를 리턴하는 get_code 메서드
    def get_code(self):
        return self.code
a=stock1('','')
a.set_name("삼성전자") #종목명을 입력
a.set_code("005939") # 종목코드를 입력
print(a.name); # name 변수에 저장되어 있는 값을 출력
print(a.code); # code 변수에 저장되어 있는 값을 출력
print(a.get_name()) #name 변수에 저장되어 있는 값을 get_name메서드를 사용하여 리턴 후 출력
print(a.get_code()) #code 변수에 저장되어 있는 값을 get_code메서드를 사용하여 리턴 후 출력
#삼성 = stock1("삼성전자","122211")
#print(삼성.name)
#print(삼성.code)
