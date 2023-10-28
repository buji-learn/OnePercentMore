"""
예외 처리
1. 조건문
2. 예외 구문

try:
    예외 발생 가능성
except:
    예외 발생했을 때 실행
else:
    예외 발생 X 실행
finally:
    무조건 실행할 코드


* 파일을 불러올 때 많이 사용한다.
* 파일을 닫을 때 finally 구문을 많이 사용한다. 
"""

# EX1
def EX1():
    try:
        number_to_string = int(input("정수를 입력하시오 : "))

        print(f'입력한 정수는 : {number_to_string}이다.')

    except:
        # print(f'{number_to_string}는 정수가 아니다.') # 오류
        print("정수가 아닙니다.5.5")

# EX2
def EX2():
    list_items = ["54", "312", "29", "필터링", "100"]

    list_num = []
    for item in list_items:
        try:
            float(item)
            list_num.append(item)
        
        except:
            pass

    print("{} 리스트 내부의 숫자는".format(list_items))
    print(f'{list_num} 이다.')

# EX3
def EX3():
    try:
        number_to_string = int(input("정수를 입력하시오 : "))

        print(f'입력한 정수는 : {number_to_string}입니다.')

    except:
        # print(f'{number_to_string}는 정수가 아니다.') # 오류
        print("정수가 아닙니다.")
    else:
        print("예외가 발생하지 않았습니다.")
    finally:
        print("이 메세지는 무조건 보게 될 거예요.")

EX3()