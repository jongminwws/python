# 문자열은 문자 + 배열
lang = 'python';

print(lang[0], lang[1]);

str = '24가 1234';
# 배열의 인덱스가 양수면 앞에서 부터
# 배열의 인덱스가 음수면 뒤에서 부터
print(str[-4:]); # 1234 가 출력 됨

#문자열 치환 (바꾸기) : 소문자 a를 A로 치환
str = "abcdef12b3sawdw7c";
print(str.replace('a', 'A'));

#문자열 더하기
str1 = "3";
str2 = "4";
print(str1+str2);

# 문자열 곱하기
print("hi" * 3);

#문자열 나누기
date = "2024-05-27";
print(date.split("-"));