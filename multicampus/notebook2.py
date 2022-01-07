# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 08:44:57 2022

@author: gi930
"""
# python pandas groupby(SQL)
# 그룹연산 실행
# 성별 성적 평균, 학년별 성적 최고점수, 부서별 평균 연봉
# groupby 메서드 처리 가능

import pandas as pd
from pandas import Series, DataFrame

kimchi = pd.read_csv('C:/Users/gi930/OneDrive/바탕 화면/Multicampus/code/20211220/kimchi_test.csv',encoding='cp949')
#pd.read_csv('././code/20211220/kimchi_test.csv',encoding='cp949')

kimchi.groupby(by=None, # 그룹핑 할 컬럼(기준)
               axis = 0 # 그룹핑 연산 방향
              level = None) # 보통 여기까지 사용, # 멀티 인덱스 지원, 멀티 인덱스일 경우, 특정 레벨의 값을 그룹핑 컬럼으로 사용

kimchi.head()


kimchi.groupby(by = '판매년도', axis = 0).sum()
