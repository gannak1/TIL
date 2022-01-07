# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 10:47:04 2022

@author: gi930
"""

## 함수
def isQueueEmpty():
    global queue, front, rear,SIZE
    if front == rear:
        return True
    else:
        return False

def isQueueFull():
    global queue, front, rear,SIZE
    if (rear+1) % SIZE == front:
        return True
    else:
        return False
    
def enQueue(Data):
    global queue, front, rear
    #print('출구<--',queue,'<--입구')
    if isQueueFull():
       print('큐가 가득참!')
       return queue
    rear = (rear + 1 ) % SIZE
    queue[rear] = Data
    return 

def deQueue():
    global queue, front, rear, SIZE
    #print('출구<--',queue,'<--입구')
    if isQueueEmpty():
        print('큐가 비었습니다!')
        #rear = front = -1
        return None
    front = (front + 1) % SIZE
    #print('입장손님',queue[front])
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global queue, front, rear, SIZE
    if isQueueEmpty():
        print('큐가 비었습니다!')
        return None
    return queue[(front+1)%SIZE]


## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0


## 메인
queue = [None, None, '문별', '휘인', '선미']
front = 1
rear = 4
enQueue('재남')
print('출구<--', queue, '<--입구')
deQueue()
enQueue('유정')
print('출구<--', queue, '<--입구')
