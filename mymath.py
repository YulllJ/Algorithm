# ctrl + / 하면 선택한 줄들 다 주석 똑같이 다시하면 주석풀기
import time
def factorial (number) -> int:
    '''
    factorial by repetition
    :param number: number(int)
    :return : facotorial result(int)
    '''
    result = 1
    for i in range(1, number+1):
        result=result*i
    return result
"""
#재귀함수는 for문 같은 반복문이 없어 그냥 계속 자기를 호출함
def factorial(number) ->int:
    '''
    factorial by recursion
    '''
    if number ==1:
        return 1
    else:
        return number*factorial(number-1)

"""


# 한 함수는 하나만 기능을 해야돼 Solid(여기서 시간재는거 별개로 하면 됨)
# decorator로 해야돼(수정에는 닫혀있거 확장에는 열려있는 개방폐쇄를 따라야 한다)

# closure decorator
def timer(func):#성능 체크할때 써먹을 함수
    def wrapper(* args, **kwargs):
        start = time.time()
        result=func(*args, **kwargs)
        end = time.time()
        print(f"time elapsed:{end - start}")
        return result
    return wrapper  # 괄호없이 함수 이름만 리턴함


@timer
def nCr(n, r) -> int:
    numerator = factorial(n)
    denominator = factorial(n - r) * factorial(r)
    return int(numerator / denominator)
# 순수 조합 기능만 하도록 코드를 수정한 것
