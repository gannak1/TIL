# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:17:10 2021

@author: gi930
"""

# 시각화
import pandas as pd
import numpy as np
from pandas import Series,DataFrame

df1 = pd.read_csv('C:/Users/gi930/OneDrive/바탕 화면/Multicampus/code/20211227/cancer_test.csv')
df1.columns
df1.dtypes

df1.head()
df1.info()
df1.describe()

# 1.radius_mean, texture_mean, texture_se, smoothness_se
# NA인 행을 제거한 후 총 핻ㅇ의 수 리턴

df1['radius_mean'].isnull().sum()   # 4
df1['texture_mean'].isnull().sum()  #4
df1['texture_se'].isnull().sum()    #4
df1['smoothness_se'].isnull().sum() #4

vbool = df1['radius_mean'].isnull() & df1['texture_mean'].isnull() & df1['texture_se'].isnull() & df1['smoothness_se'].isnull()
vbool.sum()

df1
df1.loc[vbool,:]

df1.shape # (569,320)
df1.shape[0] # 행의 개수
df1.shape[1] # 열의 개수

df1.shape[0]-vbool.sum() # 565 --> not null 행수

print(df1.shape[0]-vbool,sum())

# dropna
df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'],how='all')
df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'],how='all').shape[0]
nrow = df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'],how='all').shape[0]
print(nrow)

# 2. concavity_mean 의 standard scaling(표준화) 후, 결과가 0.1 이상인 값의 개수 추렭해줘\
# standard scaling(표준화) = (원데이터 - 평균) / 표준편차
# minmax scaling = (원 데이터 - 최소) / (최대-최소)

df1.columns
(df1['concavity_mean']-df1['concavity_mean'].mean()) / df1['concavity_mean'].std()
vscale = (df1['concavity_mean']-df1['concavity_mean'].mean()) / df1['concavity_mean'].std()
(vscale >= 0.1).sum() # 207

#(df1['concavity_mean']-df1['concavity_mean'].min()) /( df1['concavity_mean'].max() - df1['concavity_mean'].min())

# 이상치 건 수 확인
# 3. texture_se 의 상위 10% 값(NA를 제외한 건수의 10%)을 이상치로 가정한다.
#    10%를 제외한 값의 최대값으로 수정한 후 평균을 소수점 둘째자리로 반올림하여 출력

# 이상치 건수 확인
df1['texture_se'].dropna().shape[0] # 565
nx = int(np.trunc(df1['texture_se'].dropna().shape[0] * 0.1)) #56 # trunc 행렬안에 
type(nx) # 정수

# 이상치를 제외한 나머지 >> 평균
df1['texture_se'].rank(ascending = False, method='first')
vrank = df1['texture_se'].rank(ascending = False, method='first')
df1.loc[vrank > nx, 'texture_se'] # 정상치 데이터
df1.loc[vrank > nx, 'texture_se'].max() # 정상치 데이터 최대값
df1.loc[~(vrank > nx), 'texture_se'] # 이상치 데이터
df1.loc[vrank < nx, 'texture_se'] # 이상치 데이터
df1['texture_se'].sort_values(ascending=False)[:nx]

# 이상치 데이터를 vmax 치환
vmax = df1.loc[vrank > nx, 'texture_se'].max()

df1.loc[vrank < nx, 'texture_se'] = vmax

round(df1['texture_se'].mean(),2)


# 4. symmetry_mean의 결측치를 최소값으로 수정한 후 평균을 소수점 둘째자리로 반올림 하여 출력해 주세요
df1['symmetry_mean'].min() # '-' 문자열이 존재

from numpy import nan as NA
df1['symmetry_mean'].replace('.',NA)
df1['symmetry_mean'] = df1['symmetry_mean'].replace(['-','.','pass'],NA)
df1['symmetry_mean'] = df1['symmetry_mean'].astype('float')

# 최소값 확인
vmin = df1['symmetry_mean'].min()

# 결측치 수정
df1['symmetry_mean'].fillna(vmin)
df1['symmetry_mean'] = df1['symmetry_mean'].fillna(vmin)

# 평균 확인
print(round(df1['symmetry_mean'].mean(),2))

round()

# 참고 

a = np.array([-1.7,-1.5,-0.2,0.2,1.5,1.7,2.0])
np.trunc(a)

_df = pd.DataFrame(
    {'name': ['KIM', 'LEE', 'SMITH','BROWN', 'MILLER'],
     'age': [24, 32, 43, 24, np.nan]})

'''
     name   age
0     KIM  24.0
1     LEE  32.0
2   SMITH  43.0
3   BROWN  24.0
4  MILLER   NaN

'''
_df['rank_average'] = _df['age'].rank(method='average')
_df['rank_min'] = _df['age'].rank(method='min')
_df['rank_max'] = _df['age'].rank(method='max')
_df['rank_first'] = _df['age'].rank(method='first')
_df['rank_dense'] = _df['age'].rank(method='dense')
# dense는 min과 유사, 그룹간 순위 1씩 증가
_df['age'].rank(method='first')
_df['age'].rank(method='first',ascending=False)
