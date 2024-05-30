# message 함수 선언
#def message():
#    print("A")
#    print("B")

# message 함수 호출
#message()
#print("C")
#message()

#def hello(a):
#    print(a)
    
#hello("안녕")

#hello("hi")

#def add(a,b):
#    print(a+b)
    
#add("안녕",str(5))

#def add3(a,b):
#    return a+b

#add3(10,2)


# 1. 임의의 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 선언하고 호출하기

#list = [80,50,70,60,50]
#def lists(list):
#    av = sum(list) / len(list)
#    print(av)
#av = lists(list)

#2. 임의의 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 선언하고 호출하기
list = [20,55,40,80,60,71]
def print_even(list):
    for num in list:
        if num % 2 == 0:
            print(num)
print_even(list)

def n_plus_1(n):
    return n+1
result = n_plus_1(3)

print(result)

def a1(num):
    return num+4

def a2(num):
    return num*10

a= a1(10)
c= a2(a)

print(c)
list1 = ["daum", "kakao"]
ss = (input("문자 입력")); # java에서 스캐너 같은 느낌
def make_url(ss):
    if ss in list1:
        return "wwww." + ss + ".net"
    else:
        return "www."+ ss + ".com"

url = make_url(ss)
print(url)

