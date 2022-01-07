# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 09:26:45 2021

@author: gi930
"""
# python pandas groupby(SQL)
# 그룹연산 실행
# 성별 성적 평균, 학년별 성적 최고점수, 부서별 평균 연봉
# groupby 메서드 처리 가능

import pandas as pd
from pandas import Series, DataFrame

kimchi = pd.read_csv('C:/Users/gi930/OneDrive/바탕 화면/Multicampus/code/20211220/kimchi_test.csv',encoding='cp949')
pd.read_csv('././code/20211220/kimchi_test.csv',encoding='cp949')

kimchi.groupby?


kimchi.groupby(by=None, # 그룹핑 할 컬럼(기준)
               axis = 0 # 그룹핑 연산 방향
              level = None) # 보통 여기까지 사용, # 멀티 인덱스 지원, 멀티 인덱스일 경우, 특정 레벨의 값을 그룹핑 컬럼으로 사용

# 예제) 제품별, 판매처 별(김치별) 수량 총 합
kimchi.groupby(by=['제품']).sum()
#Out[5]: <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000015862D0C580>



kimchi.groupby(by=['제품','판매처'])['수량'].sum()


# 제품기준, 수량과 판매금액 총 합 구하기
kimchi.groupby(by='제품')[['수량','판매금액']].sum()
kimchi.수량.sum()

# 멀티 인덱스
kimchi_2 = kimchi.groupby(by=['제품','판매처'])['수량'].sum()

# 예제) 제품별, 판매처별(김치별) 수량 총 합, 평균
kimchi.groupby(by=['제품','판매처'])['수량'].agg(['sum','mean'])

# agg: 여러 함수들을 동시에 전달

# 예제) 제품별, 판매처별(김치별) 수량 판매금액 총합, 평균
kimchi.groupby(by=['제품','판매처'])[['수량','판매금액']].agg(['sum','mean'])


# 예제) 제품별, 판매처별(김치별) 수량은 총합, 판매금액 평균만 >> dict() 사용
kimchi.groupby(by=['제품','판매처'])[['수량','판매금액']].agg({'수량':'sum','판매금액':'mean'})

# 멀티 레벨을 갖는 경우의 groupby 연산
kimchi_2
type(kimchi_2)
# Series(9,) = (9,1)
kimchi_2.groupby(level=0).sum() # 제품별 총합
kimchi_2.groupby(level='제품').sum() # 제품별 총합
kimchi_2.groupby(level=1).sum() # 판매처별 총합
#level ~= 차원


