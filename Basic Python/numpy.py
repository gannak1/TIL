# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:26:37 2021

@author: gi930
"""

# 자료구조
# 리스트(기본구조)
# 2. 튜플(상수,불변)
# 3. 딕셔너리(key:alue) << 자바(json) {1:'ㅇㅅㅇ',2:'ㅡㅅㅡ',3:'>ㅅ<'}
# 4. 세트(set) : 집합
# 5. 배열(numpy)
# 6. 판다스 구조(Series,DataFrame)

# 넘파이
# 배열(array) 생성, 연산

#배열(array): 하나의 데이터 타입 허용(int, float), 다차원 자료구조
import numpy as np
np.array([1,2,3])
# array([1,2,3]) 1차원 배열

np.array([[1,2,3],[4,5,6],[7,8,9]])
#array([[1,2,3],
#      [4,5,6],
#      [7,8,9]])
# 2차원 배열 (수리적 모형: 행,열)

np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
#np.array([[[1,2,3],
#          [4,5,6]],
#          [[7,8,9],
#          [10,11,12]])
# 3차원 배열

np.arange(1,26)
#array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
#       18, 19, 20, 21, 22, 23, 24, 25])
np.arange(1,26).reshape(5,5)#-1을 넣으면 나머지 숫자에 맞춰서 자동으로 생성
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])

a1 = np.arange(1,26)
type(a1)

# 색인
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
#array[행 선택, 열 선택]
a2[1,:]
#array([4, 5, 6])

# 정수 색인(두번째 열 선택: 차원 축소 발생)
a2[:,1]
#array([2, 5, 8]) - reshape해서 리턴함

# 슬라이스 색인(두번 째 열 선택: 차원축소 발생 안함)
a2[:,1:2]
# array([[2],
#        [5],
#        [8]]) - 오류코드 + in platform치면 해결방법 나옴

# a2에서 1,3행 선택
a2[0:3:2,:]
a2[[0,2],:]

# a2에서 1,3 열 선택
a2[:,0:3:2]
a2[:,[0,2]]

a2
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
a2[1,1] # 5 return
a2[[1,2],[1,2]] # [5,9] return
# >>> a2[1,1],a2[2,2] 포인트 인덱싱
# 2개의 포인트(점) 출력
#색인함수 (ix()) 사용하여하여 해결

#a2[[1,2],[1,2]] 여기서 1,2행이랑 1,2열 겹치는 부분을 추출하려고 했는데 그 값이 5,9로 나와서 원하는 값을 못 얻어서 a2[np.ix_([1,2],[1,2])] 이 방법으로 하셨다는 뜻이죠?


a2[np.ix_([1,2],[1,2])]
# array([[5, 6],
#        [8, 9]])

a = np.arange(10).reshape(2, 5)
a
#ixgrid = np.ix_([0, 1], [2, 4])
#ixgrid
#ixgrid[0].shape, ixgrid[1].shape
#a[ixgrid]
#ixgrid = np.ix_([True, True], [2, 4])
#a[ixgrid]
#ixgrid = np.ix_([True, True], [False, False, True, False, True])
#a[ixgrid]
#np.ix_? 도움말

# 조건 색인
a2 > 5
#array([[False, False, False],
#       [False, False,  True],
#       [ True,  True,  True]])

a2[a2>5]
#array([6, 7, 8, 9]) True만 출력

a2[:,0] > 5 # 첫번째 컬럼 가져와서 5 이상인 행만 선택
a2[a2[:,0] > 5]
# array([[7, 8, 9]])
# 조건의 결과를 행방향에 색인 값으로 전달

#3. 메서드
dir(a2)

a2.dtype # numpy 구성하는 데이터 타입
a2.shape # numpy 모양(shape)
a2.shape[0] # numpy 행의 수
a2.shape[1] # numpy 열(컬럼) 수

a2.reshape(1,9) # array 모양 변경
a2.ndim # array 차원

4. 연산
[1,2,3] + [4,5,6]       # list는 서로 원소끼리 연산 불가 (확장으로 해석됨)
# [1, 2, 3, 4, 5, 6]
np.array([1,2,3]) + np.array([4,5,6])
# array([5,7,9])
# np.array([1,2,3]) + np.array([4,5,6,7]) #사이즈가 같아야 연산이 가능함

# 5. 형(데어티 타입) 변환 메서드

a2.astype('float')
a2.astype('int')
a2.astype('str')


#6. np.where 함수
#if문의 축약
#np.where(조건, 참인 값 반환, 거짓인 값 반환)

# sql 문 기본 형태 : select * from db where

np.where(a2>5,a2,'B')

# 7. 산술 연산 매서드
a2
a2.sum()    # 전체 합
a2.mean()   # 전체 평균
a2.var()    # 전체 분산
a2.std()    # 전체 표준편차(평균에서 떨어진 정도)
a2.min()    #전체 최소값
a2.max()    #전체 최대값

(a2 > 5).sum() # a2 에서 5보다 큰 값의 수
(a2 > 5).any() #True a2에서 5보다 큰 값이 하나라도 있으면 참
(a2 > 5).all() # False a2에서 모두 5보다 클 경우맘ㄴ 참

a2.sum(axis=0) # 행기준, 행 별 총함(서로 다른 행끼리, 세로방향 연산)
a2.sum(axis=1) # 옇기준, 열 별 총함(서로 다른 열끼리, 가로방향 연산)

# [축 번호]
# 2차원 : 행(0) 열(1)
# 3차원 : 층(0) 행(1) 열(2)

# 8. 전치 메서드
1) T : 행과 열을 전치

a1 = np.arange(1,9).reshape(4,2)
a1
a1.T

# 2) swapaxes: 두 축을 전달 받아서 두축을 서로 전치, 전달 순서는 중요치 않음
a1.swapaxes(0,1)
a1.swapaxes(1,0)

# 3) transpose
# 원본의 차원에 맞는 축번호를 인수에 차례대로 전달. 그리고 그대로 전치 전달되는 순서 중요
a1.transpose(0,1) # 원본 그대로 출력
a1.transpose(1,0) # 행과 열 전치

# 외부 파일 입출
# np.load



# np.savetxt(fnbame,      #파일명
#           X,           # 객체명
#           delimiter,   #구분자
#           fmt,         # 출력형식(format)
#           header,      # 헤더출력여부(file 첫 문자열)
#           encoding     # 인코딩옵션
           
           
x = np.arange(0.0,5.0,1.0)
np.savetxt('./data/t',x,delimiter=',',fmt='%s',header=False,encoding=U)
# '%s':문자타입(string)

#[참고 : fmt 전달/변경 방식]
# %s : 문자열
# %f : 실수(float)
# %2f : 2자리 실수
# %d : 정수(int)
# %10d : 10자리 정수