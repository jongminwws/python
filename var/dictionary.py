# 딕셔너리는 순서는 없지만, key와 value 형태로 데이터를 저장
# 1위는 닥스, 2위는 스플릿, 3위는 럭키
movie_rank = {1:"닥터스트레인지",2:"스플릿",3:"럭키"};
print(movie_rank);
# 4위로 배트맨을 추가
movie_rank[4]="배트맨";
print(movie_rank);

#4위를 배트맨에서 슈퍼맨으로 수정
movie_rank[4]="슈퍼맨";
print(movie_rank);

# 4위를 삭제
del movie_rank[4];
print(movie_rank)


# 1. 다음값을 리스트에 저장하고, 데이터의 개수를 구하여라
food_rank = ["피자","김밥","만두","양념치킨","족발","김치만두"];
print(len(food_rank));

# 2. 다음 값을 딕셔너리에 저장하거, 데이터 화면에 출력
ice = {1:"이름",2:"가격"};

ice_cream = {
    "메로나": 300,
    "비비빅": 400,
    "죠스바": 200
};

ice_cream["월드콘"] = 500;

print(f"{ice[1]} {ice[2]}") # print(f"{ice[1]} {ice[2]}")는 포맷 문자열을 사용하여 ice[1]과 ice[2]의 값을 출력
for a, b in ice_cream.items(): # ice_cream.items()는 딕셔너리의 키-값 쌍을 튜플 형태로 반환
    print(f"{a} {b}"); # print(f"{a} {b}")는 포맷 문자열을 사용하여 a과 b의 값을 출력합니다
    