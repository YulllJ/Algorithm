# 선형 리스트
# 실제 메모리는 물리적 순서가 아니라 개념적 순서 그래서 배열을 id()로 찍어보면 순서가 없다는 것을 확인이 가능하다.
# 가장 뒤에 넣어줄때는 공간 늘려주고 그 곳에 넣어주는것
# 중간에 삽입하는 경우는 중간에 공간 확보해주고 밀어서 그 안에 공간을 만들어서 그 안에 넣어줄수 있도록 하는 것

# 삽인 삭제는 오버헤드가 존재하지 않아
# 다항식의 선형 리스트 표현
'''
fx=[5,4,6,5]
polyStr= "P(x)= "
for i in range(len(fx)):
    polyStr += f"+{fx[i]}x^{len(fx)-i}"
print(polyStr)
'''

## 함수 선언 부분 ##
def print_poly(f_x) -> str:#refactor rename하면 이름 추천받아서 해줌(파이썬식 이름으로 한번에 바꿔줘?)
    term = len(f_x) - 1
    poly_expression = "P(x) = " #스네이크 이름법이 아냐??

    for i in range(len(fx)):
        coef = f_x[i]  # 계수
        if term != 0:
            if coef ==0:
                term -= 1
                continue
            if (coef > 0)& (i != 0):
                poly_expression += "+"
            poly_expression += f"{coef}x^{term} "
            term -= 1
        elif term == 0:
            if (coef > 0):
                poly_expression += "+"
            poly_expression += f"{coef}"
    return poly_expression


def calc_poly(xVal, f_x):
    return_value = 0
    term = len(f_x) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(fx)):
        coef = f_x[i]  # 계수
        return_value += coef * xVal ** term #이거 계산 우선순위가 어케 되는겨)
        term -= 1

    return return_value


## 전역 변수 선언 부분 ##
fx = [8,-1,3,2,0,5,6]

## 메인 코드 부분 ##
if __name__ == "__main__":
    print(print_poly(fx))
    print(calc_poly(int(input("X 값-->")), fx))


