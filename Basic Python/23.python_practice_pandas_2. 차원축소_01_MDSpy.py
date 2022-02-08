# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:49:38 2022

@author: gi930
"""

# 다차원 척도법(MDS)
#- 개체들 사이의 유사성, 비유사성을 거리로 측정하여 2차원/3차원 공간상에
#  점으로 표현하는 기법
#- 개체들 사이의 집단화를 시각적으로 표현하는 분석방법
#- 차원 축소과정에서 발생하는 오차(stress) 정의 
#- stress 크기로 차원 축소에 대한 적합도 판단
#- stress(0: 완벽, 5: 좋음, 10: 보통, 20: 나쁨) # 차원축소의 적합도를 나타냄 -> 오차를 나타낸다

from sklearn.manifold import MDS 

# 1. data loading 
from sklearn.datasets import load_iris
iris_x=load_iris()['data']
iris_y=load_iris()['target']

iris_x  # 변수가 4개 -->> 4차원 

# 2. Scailing 정규화
from sklearn.preprocessing import StandardScaler as standard
m_sc=standard()
m_sc.fit_transform(iris_x)
iris_x_sc=m_sc.fit_transform(iris_x)
# PCA 적용 전 스케일링 변환 

m_mds2 = MDS(n_components=2)
m_mds3 = MDS(n_components=3)


# 4. 데이터 변환
iris_x_mds1 = m_mds2.fit_transform(iris_x_sc)
iris_x_mds2 = m_mds3.fit_transform(iris_x_sc)

# 4. 유도된 인공변수 확인

m_mds2.stress_          # 235.58680425839853 --> 적합도 평가(.stress)
m_mds2.embedding_       # 변환된 데이터 셋 값

# 변환된 데이터 셋 값 --> points 변수에 담기
points = m_mds2.embedding_


# 5. 크루스칼 스트레스 계산

import numpy as np
from sklearn.metrics import euclidean_distances

DE = euclidean_distances(points) # 
DA = euclidean_distances(iris_x) # 

stress = 0.5*np.sum((DE-DA)**2) # 3523.95 # euclidean 거리 / 2
stress1 = np.sqrt(stress/(0.5*np.sum(DA**2))) # 거의 완벽하게 나옴

stress1 # 0.1857

#3 차원

m_mds3.stress_ 
m_mds3.embedding_


points = m_mds2.embedding_

# 크루스칼 스트레스 계산

import numpy as np
from sklearn.metrics import euclidean_distances



DE = euclidean_distances(points)
DA = euclidean_distances(iris_x)

strsss = 0.5 * np.sum((DE-DA)**2) 
stress # 3523.9512

stress2 = np.sqrt(stress/(0.5*np.sum(DA**2)))
stress2 # 0.1856853
