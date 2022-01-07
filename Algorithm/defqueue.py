# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 10:27:10 2022

@author: gi930
"""


## 함수
def isQueueFull():
    global queue, front, rear,SIZE
    if rear != SIZE-1:
        return False
    elif rear == SIZE-1 and front == -1:
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def isQueueEmpty():
    global queue, front, rear,SIZE
    if front == rear:
        return True
    else:
        return False

def enQueue(Data):
    global queue, front, rear
    #print('출구<--',queue,'<--입구')
    if isQueueFull():
       print('큐가 가득참!')
       return queue
    rear += 1
    queue[rear] = Data
    return 


def deQueue():
    global queue, front, rear, SIZE
    #print('출구<--',queue,'<--입구')
    if isQueueEmpty():
        print('큐가 비었습니다!')
        #rear = front = -1
        return None
    front += 1
    #print('입장손님',queue[front])
    data = queue[front]
    queue[front] = None
    return data
    
def peek():
    global queue, front, rear, SIZE
    if isQueueEmpty():
        print('큐가 비었습니다!')
        return None
    return queue[front+1]
## 전역변수
SIZE = 5
queue = [None for i in range(SIZE)]
front = rear = -1

## 메인
queue = [None, None, '문별', '휘인', '선미']
front = 1
rear = 4

enQueue('유정')
print('출구<--', queue, '<--입구')
enQueue('재남')
print('출구<--', queue, '<--입구')
enQueue('윤아')
print('출구<--', queue, '<--입구')


queue = ['화사','솔라','문별','휘인',None]
front = -1
rear = 3
print(isQueueFull())

enQueue('재남')

queue = ['화사','솔라',None,None,None]
front = -1
rear = 1
retData = peek()
print('다음 준비 손님 ==>', retData)

retData=deQueue()
print('입장 손님' , retData)
retData=deQueue()
print('입장 손님' , retData)
retData=deQueue()
print('입장 손님' , retData)

