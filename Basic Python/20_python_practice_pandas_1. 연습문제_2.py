# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:13:00 2022

@author: gi930
"""

# card.csv 파일 읽기

import pandas as pd

pd.read_csv('C:\\Users\\gi930\\OneDrive\\바탕 화면\\Multicampus\\code\\20211227\\card.csv',encoding='cp949')
card = pd.read_csv('C:\\Users\\gi930\\OneDrive\\바탕 화면\\Multicampus\\code\\20211227\\card.csv',encoding='cp949')
# NUM을 인덱스로 사용
card = card.set_index('NUM')

# 문제 ) 일자별 총 지출 금액을 구해서, 마지막 컬럼에 추가
# (천 단위 구분기호 제거 후 숫자 컬럼 변경하시오)

card
# 행/가 열/세
card.sum(axis =0) # default : axis=0 세로방향
card.sum(axis =1) 
# 서로 드란 열끼리 (가로방향) 덧셈
# 문자 타입이라 문자열 결합

# ',' 문자 제거 >> 숫자 변경
# 천단위; 구분기호 제거 >> 숫자 컬럼 변경
'19,400'.replace(',','')
int('19,400'.replace(',',''))

#'19,400'.replace(',','').astype('int')
# 문자열 사용불가(array,Series,DataFrame 사용 가능)
card = card.applymap(lambda x : int(x.replace(',','')))

# applymap : 2차원 데이터 셋(DataFrame)에 함수 적용 위해 사용

# int('19,400'.replace(',',''))
# 이 행위(형변환 함수)를 적용 할 때 사용

# 일자별 총 합 (새로운 열 생성)
card['총합'] = card.sum(axis = 1)

# [참고 - 위 함수들 특정 컬럼에 대해 적용]

card_new = pd.read_csv('C:\\Users\\gi930\\OneDrive\\바탕 화면\\Multicampus\\code\\20211227\\card.csv',encoding='cp949')
card_new = card_new.set_index('NUM')

# - 식료품 컬럼에만 적용
#card_new['식료품'].applymap(lambda x : int(x.replace(',','')))
# 1차원 데이터 셋(Series) 에 적용 불가
card_new['식료품'] = card_new['식료품'].map(lambda x : int(x.replace(',','')))
 
card_new['의복'] = card_new['의복'].str.replace(',','').astype('int')

card_new['책값'].replace(',','')
# 값 치환 메서드(특정 값과 정확히 일치하는 값을 변경하거나 삭제)
# ','와 완전히 일치하는 값을 변경 또는 삭제
card_new['책값'].replace('28,000','')

# 2) 일자별로 각 품목별 지출 비율을 출력하세요(%로 출력하세요)
card = pd.read_csv('C:\\Users\\gi930\\OneDrive\\바탕 화면\\Multicampus\\code\\20211227\\card.csv',encoding='cp949')
card = card.set_index('NUM')

card = card.applymap(lambda x : int(x.replace(',','')))

# 첫번째 행에 대해 확인
card.iloc[0,:]
card.iloc[0,:].sum()

(card.iloc[0,:] / card.iloc[0,:].sum()) * 100
# ctrl 1 주석처리

# appy 메서드 이용, 각 일자별로 적용 (썩은물 전용)
card.apply(lambda x : x / x.sum()*100,axis = 1).mean()

# 결과 해석
# - 의복비 지출이 심함 (일자별 지출 중 의복비 비중이 50% 이상)
# insight (통찰) 의복비 비중을 줄일 필요성이 있음(주관적 의견)

# 형(데이터 타입) 변환 : 항수, astype 메서드
# 적용함수 : map 함수, map 메서드, apply 메서드, appymap 메서드
# 치환함수 : 문자열 메서드, 벡터화 내장된 문자열 메서드
# 색인 find()
# 컬럼 추가, 컬럼 내용 변경

# 문제( 각 구매 마다 포인트 확인하고, POINT 컬럼 생성
# POINT 는 주문금액 50000 미만 1%, 5만 이상 10만 미만 2%, 10만 이상 3%
# 문제 풀이 포인트 : 조건에 따른 치환 혹은 연산

df1 = pd.read_csv('C:\\Users\\gi930\\OneDrive\\바탕 화면\\Multicampus\\code\\20211220\\ex_test1.csv',encoding='cp949')
# if df1['주문금액']< 50000:
#     df1['주문금액'] * 0.01
    
# if 문은 여러개의 T/F (boolean) 연산 불가

for i in df1['주문금액']:
    if i < 50000:
        i * 0.01
    elif i < 100000:
        i * 0.02
    else:
        i * 0.03
result = []


for i in df1['주문금액']:
    if i < 50000:
        result.append(i * 0.01)
    elif i < 100000:
        result.append(i * 0.02)
    else:
        result.append(i * 0.03)
import numpy as np       
print(result)
print(np.round(result,2))


df1['point'] = np.round(result,2)
df1

# sol2) np.where(벡터 연산 가능한 조건 연산 함수)
# sql에서 copy함
# sql : select * from db_name where 조건절
# np.where(조건, 참 리턴, 거짓 리턴)

# np.where(df1['주문금액'<50000, df['주문금액' * 0.01,df1['주문금액']*0.02]])
np.where(df1['주문금액']< 50000,                # 첫번째 조건
         df1['주문금액']*0.01,                  # 첫번째 조건이 참이면 연산하세요
         np.where(df1['주문금액']<100000,       # 두번째 조건
                  df1['주문금액']*0.02,         # 두번째 조건이 참이면 연산하세요
                  df1['주문금액']*0.03))        # 두번째 조건이 거짓이면 연산

# 첫번째 조건이 거짓이면, 새로운 조건 추가\
    
df1['point2']=np.where(df1['주문금액']< 50000,df1['주문금액']*0.01,np.where(df1['주문금액']<100000,df1['주문금액']*0.02,df1['주문금액']*0.03))

df1.groupby('회원번호')[['주문금액','point']].sum()

# [ 연습문제 - Y 값을 서로 다른 숫자로 변경 ]
# 출제의도 : 조건에 따른 치환

df2 = DataFrame({'Y':['a','a','b','b','c','a','b','b'],
           'X1':[1,2,4,4,6,3,5,4],
           'x2':[10,30,43,34,43,43,94,32]})

df2

# 하나 씩 사용자가 치환 (정수 인덱스)
df2['Y'].replace({'a':0,'b':1,'c':2,})

# 자동 변환 함수
from sklearn.preprocessing import LabelEncoder

m_lb=LabelEncoder()
m_lb.fit_transform(df2['Y'])

# [연습문제 - 조건에 따른 값의 수정]
# df2에서 X1이 5 이상일 경우, X1 평균으로 수정(최빈값, 중앙값, 최소값)

df2['X1'][df2['X1']>5] = df2['X1']

df2.loc[df2['X1']>=5,'X1'] # 추천

df2
m1 = df2['X1'].mean()
m2 = df2['X1'].median()
m3 = df2['X1'].mode() # 최빈값
m4 = df2['X1'].mode()[0]
m5 = df2['X1'].min()
m6 = df2['X1'].max()


import statistics as stat
stat.mode(df2['X1']) # 4: 하나의 상수로 리턴해줌(int)

df2 = DataFrame({'Y':['a','a','b','b','c','a','b','b'],'X1':[1,2,4,4,6,3,5,4],'x2':[10,30,43,34,43,43,94,32]})
df2
df2.loc[df2['X1']>=5,'X1']
df2.loc[df2['X1']>=5,'X1'] = m3 # 최빈값으로 치환하겠다는 의미
# 어라, NA로 수정이 되네(문제 발생)

df2.loc[df2['X1']>=5,'X1'] = m4
df2
