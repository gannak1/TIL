# 단순선형회귀분석

?runif
x<-runif(10) # 10개의 난수 발생 
x
y<-runif(10)
y

runif(10)

set.seed(12) # 동일한 난수를 계속 생성하고자 할 때 set.seed 설정 
runif(10)

# runif : random Uniform (distribution) 균등 분포 난수
# runif(n, min, max)

runif(10, 0, 3) # 10개의 난수 발생, min=0, max=3 인 경우 

# rnorm : 정규분포에서 난수를 생성하는 함수
# rnorm(n, mean, sd)

rnorm(10, 0, 0.2) # 10개의 난수 생성, 평균=0, 표준편차=0.2

X<-runif(10)
y<-2+3*x+rnorm(10,0,0.2) 
df<-data.frame(x,y)
df

# lm(linear model): lm(종속변수~독립변수, 적용할 데이터)

lm(y~x, data=df)

#lm(formula = y ~ x, data = df)

#Coefficients:
#  (Intercept)            x  
#    1.933              2.985
# intercept: 상수, x:회귀계수 
# y=2.985x+1.933  y = bx+b0+e





