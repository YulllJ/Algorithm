#여기 예제 문제 출판사 답지 있으니까 보고 제대로 확인하기
## 클래스와 함수 선언 부분 ##
'''
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def makeSimpleLinkedList(namePhone) :
	global memory, head, current, pre
	printNodes(head)

	node = Node()
	node.data = namePhone
	memory.append(node)
	if head == None :			# 첫 번째 노드일 때
		head = node
		return

	if head.data[0] > namePhone[0] :	# 첫 번째 노드보다 작을 때
		node.link = head
		head = node
		return

	# 중간 노드로 삽입하는 경우
	current = head
	while current.link != None :
		pre = current
		current = current.link
		if current.data[0] > namePhone[0]:
			pre.link = node
			node.link = current
			return

	# 삽입하는 노드가 가장 큰 경우
	current.link = node

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = [["지민", "010-1111-1111"], ["정국", "010-2222-2222"], ["뷔", "010-3333-3333"], ["슈가", "010-4444-4444"], ["진", "010-5555-5555"]]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	for data in dataArray :
		makeSimpleLinkedList(data)

	printNodes(head)
##########위 코드 수정해야됨
'''
"""
# 원형연결리스트
# 이제 마지막이 none이 아니라 가장 첫번째로 가리킴 object를 가리키는 거니까 link=node가 되는 것
# 첫번째에 새노드 생기면 첫번째는 기존 첫번째 가리키고 마지막은 새로운애 가라키면 돼
# head가 아닐때까지 증가
## 클래스와 함수 선언 부분 ##
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start):
	current = start
	if current.link == None :
		return
	print(current.data, end=' ')
	while current.link != start:
		current = current.link
		print(current.data, end=' ')
	print()
def delete_nodes(delete_data):
	global memory, head, current, pre
	if head.data == delete_data:
		current = head
		head = head.link
		last = head
		while last.link != current :
			last = last.link#current link 아닐때까지 계속 이동하는 것
		last.link = head
		del(current)
		return
def insertNode(findData, insertData) :
	global memory, head, current, pre

	if head.data == findData :		# 첫 번째 노드 삽입
		node = Node()
		node.data = insertData
		node.link = head
		last = head		# 마지막 노드를 첫 번째 노드로 우선 지정
		while last.link != head :	# 마지막 노드를 찾으면 반복 종료
			last = last.link	# last를 다음 노드로 변경
		last.link = node		# 마지막 노드의 링크에 새 노드 지정
		head = node
		return

	current = head
	while current.link != head :	#is not None 대신 head가 들어감	# 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	node = Node()			 # 마지막 노드 삽입
	node.data = insertData
	current.link = node
	node.link = head
def find_node(find_data) :
	global memory, head, current, pre

	current = head
	if current.data == find_data :
		return current
	while current.link != head :
		current = current.link
		if current.data == find_data :
			return current
	return Node()	# 빈 노드 반환

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()
	node.data = dataArray[0]	# 첫 번째 노드
	head = node
	node.link = head
	memory.append(node)

	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		node.link = head
		memory.append(node)

	printNodes(head)

	delete_nodes("다현")
	printNodes(head)

	delete_nodes("사나")
	printNodes(head)

	delete_nodes("정연")
	printNodes(head)
	print(find_node("쯔위"))
	print(find_node("인하"))
# delete 할때 어떻게 해야할까
# 검색은 node가 head아닐때까지 가서 찾으면 됨
"""

# 원형 연결 리스트 응용 문제
import random
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def process_minus(datas):
	odd_count=0
	even_count =0
	for data in datas:
		if data % 2 == 0 :
			even_count += 1
		else :
			odd_count += 1
	print(even_count, odd_count)
	if even_count > odd_count :
		for i in range(len(datas)):
			if(datas[i] % 2) ==0 :
				datas[i] *= -1
	else:
		for i in range(len(datas)):
			if(datas[i] % 2) ==1 :
				datas[i] *= -1

	print(data_array)

if __name__ == "__main__" :
	data_array=[]

	data_array=[random.randint(1,100)for _ in range(7)]#list comprehension으로 줄여서 쓸수있어
	print(data_array)
	process_minus(data_array)
	#원형 연결 리스트 만들기
	node=Node()
	node.data=data_array[0]
	head=node
	node.link = head

	for data in data_array[1:]:
		pre=node
		node=Node()
		node.data=data
		node.link=head
	print(data_array)