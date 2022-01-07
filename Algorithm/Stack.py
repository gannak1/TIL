# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:15:20 2022

@author: gi930
"""

## 함수
def isStackFull():
    global SIZE,stack,top
    if (top >= SIZE-1):
        return True
    else:
        return False

def isStackEmpty():
    global SIZE,stack,top
    if (top <= -1):
        return True
    else:
        return False

def push(data):
    global top, stack
    if isStackFull():
        print('스택 꽉참!')
        return
    top += 1
    stack[top] = data
    return

def pop():
    global top,stack,SIZE
    if isStackEmpty():
        print('스택 없음!')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

# 전역 변수
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

## 메인
push('맥주')
top

pop()
top
