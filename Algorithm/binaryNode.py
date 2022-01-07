# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 13:29:19 2022

@author: gi930
"""

## 함수
class TreeNode():
    def __init__(self):
        self.data =None
        self.left = None
        self.right = None


## 전역

memory = []
root = None
nameAry = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']


## 메인

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)
for i in nameAry[1:]:
    node = TreeNode()
    node.data = i
    
    current = root
    while True:
        if i < current.data:
            if current.left == None :
                current.left = node
                break
            current = current.left
        else:
            if current.right == None :
                current.right = node
                break
            current = current.right
    memory.append(node)
    
print('이진 탐색 트리 구성 완료')
root.left.data
findName = '흰눈이'

current = root
while True:
    if current.data == findName:
        print(findName,'찾았음.')
        break
    elif current.data > findName:
        if current.left == None:
            print('이 트리에 없습니다.')
            break
        current = current.left
    else:
        if current.right == None:
            print('이 트리에 없습니다.')
            break
        current = current.right