# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:13:21 2021

@author: gi930
"""

#시험에 안나옴
run my_modules

import matplotlib.pyplot as plt

# 선그래프 : plot

plt.plot([1,2,3,4],
         [10,20,30,40],
         marker='^',
         linestyle='--',
         color = 'r')

s1 = Series([10,20,30,40])
s1.plot()

s1.plot(xticks=[0,1,2,3], # 눈금 좌표
        ylim=[0,100],     # y축 범위
        xlabel='x name',  # x축의 이름
        ylabel='y name',  # y축의 이름
        rot=90,           # rotation 회전 90도
        title='name',     # title 그림 제목
        marker='^',       # 마커
        linestyle='--',   # 선 스타일
        color='red')      # 컬러


plt.xticks(ticks=[0,1,2,3], labels=['a','b','c','d'], rotation = 45)

plt.xticks(ticks=[0,1,2,3], labels=['a','b','c','d'])

plt.ylim([0,100])
plt.ylabel('y_name', rotation = 0,loc='top',labelpad=30, fontdict= font1 )

# fontdict
font1 = {'family' : 'Malgun Gothic',
         'weight' : 'bold',
         'size' : 15,
         'color' : 'red',
         'style' : 'italic'}

# global option 변경
plt.rc('font',family='Malgun Gothic')


# 데이터 프레임의 선 그래프 출력

df1 = DataFrame({'apple':[10,20,30,40],'banana':[49,39,30,12],'mango':[10,32,43,40]})

df1.index = ['a','b','c','d']
df1.index.name='지점'
df1.columns.name='과일명'
df1

df1.plot() # 컬럼별 서로 다른 선 그래프 출력가능
plt.legend(fontsize=9,loc='best',title='과일 이름') # loc='best' 빈공간에 가장 좋은값을 찾아서 채움

# Bar plot
kimchi = pd.read_csv('../code/20211220/kimchi_test.csv',encoding='cp949')
kimchi = kimchi.pivot_table(index='판매월',columns='제품',values='수량',aggfunc='sum')

kimchi.plot(kind='bar')
plt.title('김치별 판매수량 비교')
plt.ylim([0,300000])
plt.ylabel('판매수량')
plt.legend(fontsize=9,loc='best',title='김치별')
plt.xticks(rotation = 0)

#-------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------
# 3. pie chart (원형차트) 조직의 구성비율을 알고 싶을때 사용 5개이상이면 지저분해진다.

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
colors = ['#d96353', '#53d98b', '#53a1d9', '#fab7fa']   #hex number
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
explode = [0.1, 0.1, 0.1, 0.1]
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(ratio,                  # 각 파이 숫자 퍼센테이지
        labels=labels,          # 각 파이 이름 
        autopct='%.1f%%',       # 값의 표현 형태(소수점 첫째자)
        startangle=260,         # 시작위치
        radius = 0.8,           # 파이 크기
        counterclock=False,     # 시계방향 진행 여부
        explode = explode,      # 중심에서 벗어나는 정도 설정(각각 서로 다른 숫자 전달 가능)
        colors=colors,          # 컬러맵 전달 가능
        shadow=False,           # 그림자 설정
        wedgeprops=wedgeprops)  # 부채꼴 모양 설정
#https://matplotlib.org/stable/tutorials/colors/colormaps.html color map

'''
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')


# make data
x = [1, 2, 3, 4]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

# plot
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
'''

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot') # R에서의 기능


# make data
x = [1, 2, 3, 4]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x))) #linspace = 일정한 길이로 나눠서 만듬

# plot
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

#-------------------------------------------------------------------------------------------------------------------------------------------
# 4. hist : 히스토그램 (밀도 표현, 전체 합 = 1)
Series(np.random.rand(1000)).hist() #uniform distribution

s1 = Series(np.random.randn(1000)) # randn : 정규분포에서 무작위 추출 rand : uniform하게 랜덤하게 나옴
s1.hist()
s1.hist(bins = 4) # 막대의 개수 또는 계급의 구간 전달

plt.hist(s1,
         bins = 5,
         density= True  # True로 설정시, 막대 아래 총 면적이 1이 되는 밀도함수 출력
                        # 즉, y 축 값이 확률로 변경되어 출력됨
         )
plt.hist(s1, density=False) #  개수로 출력
s1.plot(kind='kde')     # 커널 밀도 함수(kernel density estimation) 출력
                        # 연속형 히스토그램

#-------------------------------------------------------------------------------------------------------------------------------------------
# 5. scatter (산점도)

# iris data loading
from sklearn.datasets import load_iris

iris = load_iris()
iris.keys()
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])

iris['DESCR']
iris_x=iris['data']
x_names = iris['feature_names']


plt.subplot(2,2,1) # 2*2 그래프 중 1번째
plt.scatter(iris_x[:,0], # x축 좌표 (첫번째 설명변수)
            iris_x[:,1]) # y축 좌표 (두번째 설명변수)
# color 설정 안 할 시, 모두 동일한 색


plt.scatter(iris_x[:,0], # x축 좌표 (첫번째 설명변수)
            iris_x[:,1], # y축 좌표 (두번째 설명변수)
            c=iris_x[:,1]) # color
# 서로 다른 숫자 전달 시, 서로 다른 색으로 표현이 됨(채도)

plt.spring()
plt.xlabel(x_names[0])
plt.ylabel(x_names[1])
plt.colorbar()#컬러바 출력시

plt.subplot(2,2,2) # 2*2 그래프 중 2번째
plt.scatter(iris_x[:,1], iris_x[:,2], c=iris_x[:,2])
plt.summer()
plt.xlabel(x_names[1])
plt.ylabel(x_names[2])
plt.colorbar()
                    
plt.subplot(2,2,3) # 2*2 그래프 중 3번째
plt.scatter(iris_x[:,2], iris_x[:,3], c=iris_x[:,3])
plt.autumn()
plt.xlabel(x_names[2])
plt.ylabel(x_names[3])
plt.colorbar()

plt.subplot(2,2,4) # 2*2 그래프 중 4번째
plt.scatter(iris_x[:,3], iris_x[:,0], c=iris_x[:,0])
plt.winter()
plt.xlabel(x_names[3])
plt.ylabel(x_names[0])
plt.colorbar()

#-------------------------------------------------------------------------------------------------------------------------------------------
# 6. boxplot

plt.boxplot(iris_x)
plt.xticks(ticks=[1,2,3,4], labels=x_names)
