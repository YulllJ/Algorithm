# ctrl + / 하면 선택한 줄들 다 주석 똑같이 다시하면 주석풀기
"""
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


def nCr(n, r) -> int :
    numerator=factorial(n)
    denominator=factorial(n-r)*factorial(r)
    return int(numerator/denominator)

if __name__=="__main__":
    # n=int(input("Input n: "))
    # r=int(input("Input r: "))
    # print(f'{n}C{r}={nCr(n,r)}')
    f=int(input())
    print(factorial(f))

# 재귀함수는 안에서 자기를 호출하는 형식
# 재귀함수 호출 500번 넘어가면 컷다운함
# 재귀함수는 똑같은 일을 하지 않음 같은게 있으면 return 을 시켜서 이전에 함수들이 받는다?
# 성능은 무지하게 느려, depth때문에 안돌아가기도 RAM을 안쓰고 ALU로 계산해서 바로 써서 간단하지만 재귀함수는 아니라는 말인건가?