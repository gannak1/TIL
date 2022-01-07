# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:48:20 2022

@author: gi930
"""

## 함수/클래스 선언부
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNode(start):
    current = start
    print(current.data,end='   ')
    while current.link != None:
        current = current.link
        print(current.data,end = '   ')

def insertNode(findData,insertData):
    global memory, head, current,pre
    if head.data == findData:# 첫 노드 앞에 샆입할 때
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    # 사나 앞에 솔라를 삽입
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    # 마지막에 추가할 때(삽입할 이름이 존재하지 않을때)
    node = Node()
    node.data = insertData
    current.link = node
    return
    
def deleteNode(deleteData):
    global memory, head, current,pre
    if deleteData == head.data: # 첫 노드 삭제
        current = head
        head = head.link
        del(current)
        return
    # 첫 노드 외의 노드 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return
    
def findNode(findData):
    global memory, head, current,pre
    current = head
    if head.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    return Node()





## 전역 변수
memory = []
head, current, pre= None,None,None
dataArray=['다현','정연','쯔위','사나','지효']


## 메인 코드부
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)
for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
printNode(head)



insertNode('다현','화사')
printNode(head)

insertNode('사나','솔라')
printNode(head)


insertNode('재남','냄새꼬')
printNode(head)

deleteNode('화사')
printNode(head)

deleteNode('쯔위')
printNode(head)



fnode = findNode('다현')
print(fnode.data)
fnode = findNode('사나')
print(fnode.data)
fnode = findNode('재남')
print(fnode.data)
