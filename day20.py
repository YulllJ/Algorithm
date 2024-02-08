'''
import mymath as mm # as mm 안하면 그냥 fullname 다 적고 해야한다.
import time # time을 재는 함수
if __name__=="__main__":
    n=int(input("Input n: "))
    r=int(input("Input r: "))
    print(f'{n}C{r}={mm.nCr(n,r)}')
'''
    # f=int(input())
    # print(mm.factorial(f))
# 컴퓨터에 따라 성능이 달라 동일 성능을 가졌다고 가정하고 시간 복잡도를 계산할때 횟수로 얘기를 하게됨
# factorial 계산이 재귀함수 안쓰는게 훨씬 빨라
# 재귀함수는 안에서 자기를 호출하는 형식
# 운영체제가 레지스터에 많이 쓰는거 가져다놓고 스케쥴링을 하는 것 컴파일러는 최적의 코드로 짜주는것 빠르려면 레지스터랑 cpu랑 왔다갔다 해야됨
# 재귀함수 호출 500번 넘어가면 컷다운함 (재귀함수는 창고에 있는 함수와 같아, 느리다)
# 재귀함수는 똑같은 일을 하지 않음 같은게 있으면 return 을 시켜서 이전에 함수들이 받는다?
# 성능은 무지하게 느려, depth때문에 안돌아가기도 RAM을 안쓰고 ALU로 계산해서 바로 써서 간단하지만 재귀함수는 아니라는 말인건가?
# operation이 일어나는 횟수로 알고리즘의 성능을 측정한다.
# big O, thetha , omega 등이 존재한다.(worst case를 기록해두는 것)
# factorial이 제일 느리다.(O(n!))
# 로그 밑이 2(bit단위라 0 아니면 1이니까)  단위가 operation(실행횟수)이니까 자연수이다.
# 숫자 맞추기 게임 0에서 100까지 게임 몇번만에 맞췄는지 테스트
import random
target=random.randrange(1,100)
count=0
while True:
    mine=int(input("숫자를 입력하세요"))
    if target == mine:
        print("숫자를 맞혔습니다!")
        count += 1
        print(f'{count}번째에 맞혔습니다')
        break
    elif target!= mine:
        count += 1
        if target >mine :
            print("up")
        elif target < mine :
            print("down")
    else :
        print("다시 입력하세요")
