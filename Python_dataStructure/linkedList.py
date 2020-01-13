class Node : #노드 클래스 생성
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def init(): #연결 리스트 생성
    global node1
    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
def print_list(): #연결 리스트 출력
    global node1
    node = node1
    
    while node:
        print(node.data)
        node = node.next
    print()

def delete(del_data): #연결 리스트 데이터 삭제 후 나머지 연결
    global node1
    pre_node = node1
    next_node = pre_node.next
    
    if pre_node.data == del_data : #노드1 삭제 시
        node1 = next_node
        del pre_node
        return
    
    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next

def insert(ins_data): #연결 리스트 데이터 추가
    global node1
    new_node = Node(ins_data)
    new_node.next = node1
    node1 = new_node

def LinkedList():
    init();
    delete(3)
    insert('9')
    print_list()

LinkedList() #연결 리스트 실행