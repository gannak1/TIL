# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 09:26:26 2022

@author: gi930
"""


        

## 함수




## 전역변슈
queue = [None for i in range(5)]
front = rear = -1





## 메인
rear += 1
queue[rear]='화사'
rear += 1
queue[rear]='솔라'
rear += 1
queue[rear]='문별'
queue

print('출구<--', queue, '<--입구')

# 입장하세요.
front += 1
print('입장손님',queue[front])
queue[front] = None

front += 1
print('입장손님',queue[front])
queue[front] = None

front += 1
print('입장손님',queue[front])
queue[front] = None
queue
