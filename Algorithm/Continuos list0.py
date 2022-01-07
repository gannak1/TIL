# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:12:50 2022

@author: gi930
"""

class Node():
    def __init__(self):
        self.data = None
        self.link = None
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node5 = Node()

node1.data = '다현'
node2.data = '정연'
node3.data = '쯔위'
node4.data = '사나'
node5.data = '지효'
node1.link = node2
node2.link = node3
node3.link = node4
node4.link = node5

newnode = Node()
newnode.data = '재남'
newnode.link = node2.link
node2.link = newnode
node2.link = node3.link
del node3


'''
print(node1.data,end='   ')
print(node1.link.data,end='   ')
print(node1.link.link.data,end='   ')
print(node1.link.link.link.data,end='   ')
print(node1.link.link.link.link.data,end='   ')
while 
'''

current = node1
print(current.data,end = '   ')
while current.link != None:
    current = current.link
    print(current.data,end='   ')
        