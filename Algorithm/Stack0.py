# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:15:20 2022

@author: gi930
"""

## 함수
def push():
        global top, stack
        top += 1
        stack[top] = ''
        return

def pop():
    global top,stack
    data = stack(top)
    stack(top) = None
    top -= 1
    return data

## 전역 변수
#stack = [None,None,None,None,None]
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

## 메인
top += 1
stack[top]='커피'
top += 1
stack[top]='녹차'
top += 1
stack[top]='꿀물'
print(stack)

data = stack[top]
stack[top] = None
top -= 1
print('팝-->',data)

data = stack[top]
stack[top] = None
top -= 1
print('팝-->',data)

data = stack[top]
stack[top] = None
top -= 1
print('팝-->',data)