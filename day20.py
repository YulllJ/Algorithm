# 연결 리스트
# 노드 들이 물리적으로 떨어진 곳에 위치
# 각노드의 번지도 순차적이진 않음 화살표로 연결된거 따라가면 선형 리스트 순서와 동일하다.
# 선형 리스트는 삽입시 시간 복잡도가 O(N)이다.(하나씩 다 옮겨줘야 하기 때문이다.)
# linked list는 삽입 삭제에서 오버헤드가 거의 복잡하지 않는다. 그냥 연결만 하면 되기 때문

# self 는 c++에서 pointer임  가리키는 거니까 linked list임
# node1.link=node2는 중요
# 같이 한군데를 가리키면 안돼
#노드=링크 하면 연결인거고 노드=노드 면 새로 할당해주는건가? 링크=노드 인경우는 이쪽은 보면서 제대로 확인을 해야할듯
#마지막은 none을 찾으면 됨(못찾으면 문별 노드를 넣어주면 된다 마지막 노드(지효가) 문별 녿를 넣어주면된다.)


## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None
#카멜 표기법을 스네이크 표기법으로 바꾸라고?
def print_nodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link is not None:
		current = current.link
		print(current.data, end = ' ')
	print()
def insert_node(find_data, insert_data) :
	global head, current, pre #함수 바깥에 있는 애들을 말하는 것

	if head.data == find_data :      # 첫 번째 노드 삽입 # 다현은 아니야
		node = Node()
		node.data = insert_data
		node.link = head
		head = node
		return

	current = head
	while current.link is not None :    # 중간 노드 삽입
		pre = current
		current = current.link# 정연으로 바뀌었음 정연은 쯔위 주소 가지고있어
		if current.data == find_data :#정연이랑 사나랑 같은지 체크
			node = Node()
			node.data = insert_data
			node.link = current
			pre.link = node
			return

	node = Node()                   # 마지막 노드 삽입
	node.data = insert_data
	current.link = node
def delete_node(delete_data) :
	global  head, current, pre

	if head.data == delete_data :         # 첫 번째 노드 삭제
		current = head
		head = head.link
		del(current)
		return

	current = head                          # 첫 번째  외 노드 삭제
	while current.link != None :
		pre = current
		current = current.link
		if current.data == delete_data :
			pre.link = current.link
			#print(current.data)
			del(current)

			return
def find_node(findData) :
	global  head, current, pre

	current = head
	if current.data == findData :
		return current
	while current.link != None :
		current = current.link
		if current.data == findData :
			return current
	return Node()	# 빈 노드 반환
## 전역 변수 선언 부분 ##
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
#main문 안이 node연결해주는 코드인것
if __name__ == "__main__" :
	node = Node()		# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node


	print_nodes(head)
	insert_node("다현", "화사")
	print_nodes(head)
	insert_node("사나", "솔라")
	print_nodes(head)
	insert_node("동균", "문별")#없는걸 찾는다면?
	print_nodes(head)
	delete_node(("다현"))
	print_nodes(head)
	print(find_node("재남").data)
	print(find_node("문별").data)
	print(find_node("사나").data)
#print로 연결된거 탐색해서 출력하는 것

#삽입 위치가 맨앞이라면?
#헤드값 조정이 필요

#삽입 위치가 중간인경우
# pre.link를 노드가 받아서 대입해주면 되겠다
#연결한 노드 찾은 다음에 삽입해주면된다.
 # 아이패드로 이쪽 ppt보면서 혼자 이해하면 될듯
 #솔라노드가 사나를 가리키게돼(4번에서)
 # 쯔위 링크는 솔라가 됨(5번에서)



#다음 수업은 2차원 배열 linked list
#빠르게 generator로 도는 코드
#반복문 쓰면 register안에서 하니까 좋은데 코드 길어지면 side effect와 가독성 문제 발생 재귀함수쓰면 변수선언 거의 안해서 좋지만 느려
#성능평가는 big oh time complexity등이 존재한다.(worst case고려하는 빅오로 사용함)
# operation 횟수를 카운트해서 시간 복잡도를 계산해내게됨(지수인지 로그인지 상수인지 등등..)
#코드 수정하고 분석하고 나서 git에 올릴예정