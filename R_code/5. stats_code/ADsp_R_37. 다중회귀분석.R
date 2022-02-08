# 다중  회귀분석

set.seed(1234)
x1<-runif(10, 0, 11)
x1
x2<-runif(10,11,20)
x2
x3<-runif(10, 1, 30)
x3
?runif
# These functions provide information about the uniform distribution on the interval from min to max
# runif generates random deviates
# runif(n, min = 0, max = 1)

y<-3+0.1*x1+2*x2-3*rnorm(10,0,0.1)

df<-data.frame(y, x1, x2, x3)
df

m<-lm(y~x1+x2+x3, data=df)
m

summary(m)

# lm(formula = y ~ x1 + x2 + x3, data = df)
# 회귀식을 표현함
# y_hat = 0.050797*(x1)+2.021962*(x2)-0.006534*(x3)+3.048352
# coefficients:
#              Estimate   Std. Error t value
#(Intercept)   3.048352   0.704047   4.330
# x1           0.050797   0.034567   1.470
# x2           2.021962   0.041839  48.327
# x3          -0.006534   0.010949  -0.597
# Pr(>|t|)    

# Estimate의 값: x1, x2, x3의 기울기 

#(Intercept)   0.00493 ** 
# x1           0.19208    
# x2          5.26e-09 ***
# x3           0.57248  

# Estimate: 회귀계수, Pr(>|t|): p-value 
# R-squared:  0.9975 (r-square: 설명력)
# p-value: 3.337e-08 (3.337*10의 -8제곱)

# y = 2.021962*x2 + 0.00493

# MASS 패키지에는 Diet 를 적용한 닭에 대한 데이터가 들어 있음.


install.packages("MASS")
library(MASS)

head(ChickWeight)
str(ChickWeight)

chick<-ChickWeight[ChickWeight$Diet==1,]
# Diet  변수가1인 모든 행의 값을 가져옴

chick
head(chick)

chick<-ChickWeight[ChickWeight$Chick==1,]

chick

head(chick)

# 시간의 경과에 따른 닭들의 무게를 단순회귀 분석
lm(weight~Time, data = chick)

m1<-lm(weight~Time, chick)
summary(m1)

'''
Call:
lm(formula = weight ~ Time, data = chick)

Residuals:
     Min       1Q   Median       3Q      Max 
-14.3202 -11.3081  -0.3444  11.1162  17.5346 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  24.4654     6.7279   3.636  0.00456 ** 
Time          7.9879     0.5236  15.255 2.97e-08 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 12.29 on 10 degrees of freedom
Multiple R-squared:  0.9588,	Adjusted R-squared:  0.9547 
F-statistic: 232.7 on 1 and 10 DF,  p-value: 2.974e-08
'''


data(cars)
head(cars)

mm<-lm(dist~speed, cars)
summary(mm)

'''
Call:
lm(formula = dist ~ speed, data = cars)

Residuals:
    Min      1Q  Median      3Q     Max 
-29.069  -9.525  -2.272   9.215  43.201 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) -17.5791     6.7584  -2.601   0.0123 *  
speed         3.9324     0.4155   9.464 1.49e-12 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 15.38 on 48 degrees of freedom
Multiple R-squared:  0.6511,	Adjusted R-squared:  0.6438 
F-statistic: 89.57 on 1 and 48 DF,  p-value: 1.49e-12
'''


# 회귀 진단을 하기 위해 plot() 사용
plot(mm)
# 회귀진단plot1: 선형성 진단결과
# 회귀진단plot2: 정규성 진단(얼마나 정규분포를 따르고 있는가 확인)
# 회귀진단plot3: 등분산성 진단 (기울기가 0인 경우가 가장 이상적)
# 회귀진단plot4: 이상관측치 진단 
# -2(-1.96)와 2(1.96) 밖의 관측치: 이상치(outlier)

nrow(cars)

women
plot(weight~height, data=women)

fit<-lm(weight~height, data=women)
fit
summary(fit)
plot(fit)


#### 다항 회귀모형 ####
fit2<-lm(weight~height+I(height^2), data=women)
plot(fit2)

### 다중 회귀모형 ####
state.x77
head(state.x77)

states<-as.data.frame(state.x77[, c("Murder", "Population","Illiteracy","Income","Frost")])
states
head(states)

fit <- lm(Murder~Population+Illiteracy+Income+Frost, data=states)
plot(fit)
summary(fit)

fit2 <- lm(Murder~Population+Illiteracy, data=states)
plot(fit2)
summary(fit2)
