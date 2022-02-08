# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:31:16 2021

@author: gi930
"""

# 07. Pandas_Series, DataFrame 

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# pandas : 2차원 정형데이터(테이블, 표, 데이터프레임

# 기본단위 : Series
# - 1차원 자료구조
# - 하나의 데이터 타입 허용

Series([1,2,3,4])
s1 = Series([1,2,3,4])
s2 = Series([1,2,3,'4'])

s3 = Series([1,2,3,4],index = ['a','b','c','d'])
#Series([1,2,3,4],['a','b','c','d'])

Series(s3,index = ['A','B','C','D'])# 이미 index가 존재하는 경우

# 새깅ㄴ (indexing)
s1[0]      # 차원축소 일어남 >> scalar 형식으로 출력
s1[0:1]    # Sereis형태로 출력

s1[[0,3]]  # 차원축소X (Series로 반환)


s3['a']
s3[['a','c']]

s3['a':'c'] # 문자의 연속 추출은 마지막 범위 포함

s1[s1 > 2]

s3.b  # 2 key indexing으로 접근 가능

# 연산
s1 + 1 # List와 다르게 각 원소마다 1을 더함

s4 = Series ([10,20,30,40])
s5 = Series ([10,20,30,40],index= ['c','d','e','f'])

s1 + s4 # key가 같은 값끼리 연산가능
s3 + s5 # key가 다른경우 모두 Na 반환
# 해당하는 key값이 없으면 NaN 반환 Na = 아예 없는 수치 NaN = 한쪽만 있지만 나머지는 Na, Dtype가 쓸 수 없는 Data
s3.add(s5,fill_value=0)    
# 양쪽 모두 존재하지 않는 key 일 경우 
# NA 반환되는 것을 방지하기 위해 fill)value 옵션 사용 적극 추천
s3 - s5
s3.sub(s5,fill_value='0') # - 연산
s3.mul(s5, fill_value=1) # * 연산
s3.div(s5, fill_value=1) # / 연산

# 기본 메소드
s1.dtype # dtype('int64')
s1.index # RangeIndex(start=0, stop=4, step=1)
s3.values # array([1, 2, 3, 4], dtype=int64)

s3[['c','d','a','b']] #색인 사용, 배치순서 변경
s3.reindex(['c','d','a','b']) # 메소드로 배치순서 변경

s3.index = ['A','B','C','D'] # index 수정
s3

s3[0] = 10 # 값 수정
s3

# DataFrame
# 2차원 자료구조 (행과 열 구조)

# 생성
d1 = {'name':['smith','will'],'sal':[900,1800]}
d1

df1 = DataFrame(d1)
df1
#    name   sal
#0  smith   900
#1   will  1800

import numpy as np
d3 = DataFrame(np.arange(1,7).reshape(2,3), index=['a','b'],columns=['col1','col2','col3']) # Series 한줄 = 열(columns)
d3

# 색인(indexing) **중요**

d3.col1
#a    1
#b    4

d3['col1']
#a    1
#b    4

d3.['col1','col2','col3']

#iloc loc **중요
# iloc : positional indexing
# loc : label indexing
d3

d3.iloc[:,0]
d3.iloc[:,0:3]
d3.iloc[:,[0,-1]]
d3.iloc[:,[0,2]]

d3.loc[:,['col1','col3']]

#조건색인 처리
d3.loc[d3.col1 ==1,:]

# 기본 메서드
d3.dtypes # 각 column 별 데이터 타입 확인
d3.index
d3.columns
d3.values

d3.columns=['A','B','C'] # 컬럼 이름 변경
d3

# 연산
d3 + 10

d4 = DataFrame({'A':[10,40],"B":[20,30],'C':[30,80]},index=['a','b'])
d5 = DataFrame({'A':[10,40],"B":[20,30]},index=['a','b'])

d3 + d5
d3.add(d5,fill_value=0)
d3.sub(d5,fill_value=0)
d3.mul(d5,fill_value=1)
d3.div(d5,fill_value=1)
d3






s3 = Series([1,2,3,4],index=['a','b','c','d'])
s3.reindex(['c','d','a','b']) # 메소드로 배치순서 변경, 만약 없으면 NaN값 반환

s3.index = ['A','B','C','D'] # index을 아예 수정

d3.iloc[:,[0,2]]

d3.loc[:,['col1','col3']]
d3.loc[d3.col1 ==1,:]

d3.index
d3.columns
d3.values