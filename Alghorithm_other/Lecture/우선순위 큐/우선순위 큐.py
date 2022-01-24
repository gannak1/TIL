# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 18:00:14 2022

@author: gi930
"""

import sys
import heapq
input = sys.stdin.readline# 여러줄을 받을때 사용

def heapsort(iterable):
    h= []
    result = []
    # 모든원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    # 힙에서 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
res = heapsort(arr)

for i in range(n):
    print(res[i])
