# <혼자 공부하는 파이썬>, 한빛미디어, 윤인성, 

# CH1
# 컴퓨터 프로그램 : 컴퓨터가 무엇을 해야할지 미리 작성한 진행 계획
# 소스 코드 source code : 프로그래밍 언어로 사람이 쉽게 읽고 이해할 수 있도록 만든 코드

# 표현식 >> 문장 >> 프로그램

import keyword
print(keyword.kwlist)

# 식별자 identifier : snake_case(definition or valuable), CamelCase(class)
# -------------------------------------

# CH2
# 구문 오류 Syntax Error : 실행 X, 대표적으로 괄호 여닫는 문제/ 따옴표 문제
#### print("큰따옴표 "안에" 큰따옴표")
#### print(type('buji-learn'))
#### print(type('buji-learn')

# 이스케이프 문자 escape character
# \n : 줄바꿈
# \t : 탭
# \\
# """\ (문자)""" : 줄간격 없음

# TypeError : 서로 다른 자료 type을 연산했을 때
"""
a = '1031'
print(type(a))
print(type(int(a)))

b = '일공삼일'
print(type(b))
print(int(type(b)))

print("문자랑 숫자를 더해볼까" + 1)
"""

# input() 입력값의 자료는 문자형
# cast : 숫자로 바꿔주기 >> int(), float()

# ValueError : 변환할 수 없는 것을 변환하려고 할 때
# print(int('문자열'))
# print(float('문자열'))


# format() 함수 ~ 문자열
# {} {}.format( , )
format1 = '{}만원'.format(5000)
format2 = '문자열 사이에 숫자 {}, 문자 {}끼워넣기'.format(11, '짜잔') 
print(format1,'\n', format2) #format2 앞에 띄어쓰기 무엇?

# 숫자 위치 변경/ 빈칸 0으로 채우기
output1 = '{:d}'.format(100)
output2 = '{:5d}'.format(200)
output3 = '{:10d}'.format(300)
print('output1 :', output1)
print('output2 :', output2)
print('output3 :', output3)

output4 = '{:05d}'.format(499)
output5 = '{:05d}'.format(599)
print('output4 :', output4)
print('output5 :', output5)

# 기호 

# 소숫점 아래 

# IndexError : {}개수와 ()안의 개수 안 맞을 때
# list_A = ['A', 'B', 'C']
# print(list_A[0])
# print(list_A[3])
print("문자열 안에 {} {}".format('"괄호"', "'넣어서'"))
# print("문자열 {} {} {}".format(1, 2))
print("문자열 {} {}".format(1, 2, 500))

# ""

# upper()
# lower()

# 파괴적 함수 (원본 변화) vs. 비파괴적 함수 (원본 변화X)

# strip() : 문자열 양 옆의 공백 제거
# lstrip(), rstrip()

# isalnum()
# isalpha()
# isidentifier()
# isdecimal()
# isdigit() 
# isspace()
# islower()
# isupper()
# >> 결과는 boolean 값

# find() : 문자열 찾기, 왼쪽부터, 처음 index
# rfind() : 오른쪽부터
# in

# split() : 문자열 잘라서 list로 반환
a = "문 자 열".split(" ")
print(a, type(a))