# 1. 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
# a = int(input("입력해보셈")); 
#print(a + 10); 

# 2. 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
#score = (input("과일 입력")); # java에서 스캐너 같은 느낌
#fruits = ["사과", "귤", "배"];
#if score in fruits:
#   print("정답입니다")
#else:
# print("오답입니다")


#3. 리스트에 주식 종목이름이 저장돼 있다.
#list = ["SK하이닉스", "삼성전자", "LG전자"]
# 저장된 문자열의 길이를 다음과 같이 출력하라
#for list in list:
#    print(len(list)); 

#4.  
#list = ['dog', 'cat', 'parrot']
#for list in list:
#    print(list,len(list))
# 5.구구단 3단을 출력하라.
#i =0;
#while i <9:
#    i += 1
#   print(i*3)

# 6. 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.
#i =0;
#while i <9:
#    i += 1
#    if i % 2 != 0:
#        print(i*3)

#7. 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.        
#i =0;
#sum=0;
#while i < 55:
#    i +=1;
#    sum += i;

#print(sum)


# 8. 리스트에서 세 글자 이상의 문자를 화면에 출력하라
list = ["I", "study", "python", "language", "!"]
for lists in list:
    if len(lists) >= 3:
        print(lists)
        

# 프로그래밍언어 문자열을 100번 화면에 출력하는 print_coins 함수를 선언
def print_coins():
    for i in range(100):
        print("프로그래밍언어")
        
# 함수 호출
print_coins();