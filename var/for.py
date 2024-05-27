# for , while

fruits = ["사과", "귤", "배"]; # 리스트

for fruit in fruits: # fruits 배열 길이만큼 반복이라서 3번 반복
    print(fruit);
    
for fruit in fruits: 
    print("#####");
    
    
    
fruits = ("사과", "귤", "배"); # 튜플

#리스트에 다음과 같은 숫자를 지정하고, 음수만 출력
nums = [3,-20,-3,44]

for num in nums: # nums 리스트에 있는 모든 값을 num변수에 저장
    if num <= 0:
        print(num)
        
        
#리스트에 다음과 같은 숫자를 지정하고, 3배수만 출력
nums = [3,100,23,44]

for num in nums: # nums 리스트에 있는 모든 값을 num변수에 저장
    if num % 3 == 0:
        print(num)
        
# 0~99 까지 순차적으로 출력
for i in range(100):
    print(i)
    
# 0~99 까지 순차적으로 출력 while
i =0;
while i <100:
    print(i)
    i = i+1;