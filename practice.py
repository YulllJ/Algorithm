
# Section 3:
arr=[]
def add_data(data):
    arr.append(None)
    arr[len(arr)-1]=data #마지막에 data삽입
def insert_data(position, data):
    if position <0 or position >len(arr):
        print("out of range")
        return
    else:
        arr.append(None)#빈칸 추가
        for i in range(len(arr)-1,position,-1): #len(arr)-1부터 position까지 1씩 줄어듦(for문은 len(arr)-1과 position같으면 돌아가지 않아)
            arr[i]=arr[i-1] #삽입이니까 뒤에서 부터 하나씩 뒤로 민다.
            arr[i-1]=None #집어넣을 공간 만들어줌
        arr[position]=data


def self3_1(function):
    def wrapped(arr, position):
        for i in range(len(arr) - 1, position - 1, -1):
            function(arr, i)
    return wrapped

@self3_1
def delete_data(arr, position):
    if position < 0 or position >= len(arr):
        print("out of range")
        return
    else:
        arr[position] = None  # data 제거
        for i in range(position + 1, len(arr)):  # 제거 했으니까 위치 옮기기
            arr[i - 1] = arr[i]
            arr[i] = None  # 옮기고 비우고 다시 채우기 반복
        del(arr[len(arr) - 1])  # 마지막 자리 치우기 (마지막을 삭제하든 중간에 삭제하든 자리 조정된후 마지막을 삭제)




#응용예제
class friend:
    def __init__(self):
        self.num= None
        self.name=None
def insert_katok(arr,friend):
    ll=[arr[i][1] for i in range(len(arr))]
    ll.append(friend.num)
    ll.sort(reverse=True)
    print(ll)
    insert_data(ll.index(friend.num), (friend.name, friend.num))
    return arr



if __name__=="__main__":
    add_data('ㄱ')
    add_data('ㄴ')
    add_data('ㄷ')
    insert_data(3, 'ㄹ')
    delete_data(arr, 2)
    print(arr)

    arr=[('다현',200),('정연',150),('쯔위',90), ('사나',30),('지효',15)]
    while True:
        friend.name=input("추가할 친구--->")
        friend.num=int(input("카톡 횟수--->"))
        insert_katok(arr,friend)
        print(arr)

'''

#응용문제 3-2
## 함수 선언 부분 ##
def printPoly(poly):
    polyStr = "P(x) = "

    for i in range(len(poly[0])):
        term = poly[0][i]  # 항 차수
        coef = poly[1][i]  # 계수

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "

    return polyStr


def calcPoly(xVal, poly):
    retValue = 0

    for i in range(len(poly[0])):
        term = poly[0][i]  # 항 차수
        coef = poly[1][i]  # 계수
        retValue += coef * xValue ** term

    return retValue


## 전역 변수 선언 부분 ##
poly = [[0, 0, 0], [0, 0, 0]]
poly[0][0]=300; poly[0][1] = 20; poly[0][2]= 0 #차수
poly[1][0]=7; poly[1][1] = -4; poly[1][2]= 5 #계수

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = printPoly(poly)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, poly)
    print(pxValue)

'''
