# 리스트는 순서가 있거, 수정 가능한 배열
movie_rank = ["닥터스트레인지" ,"스플릿","럭키"]

# 배트맨 추가
movie_rank.append("배트맨");

print(movie_rank);

# 슈퍼맨을 추가 (내가 원하는 곳에 추가 - innsert를 통해서)
movie_rank.insert(1,"슈퍼맨");

print(movie_rank);

# 럭키를 삭제
del movie_rank[3];

print(movie_rank);

# 리스트 값에서 최대값, 최소값을 구하기
num = [1,2,3,4,5,6,7]

print(max(num));
print(min(num));

# 리스트 값에서 합계
num = [1,2,3,4,5]
print(sum(num));

# 리스트 값에서 갯수를 구하기
print(len(num));

# 리스트 값에서 평균(합계/개수) 를 구하기
average = sum(num) / len(num);
print(average);