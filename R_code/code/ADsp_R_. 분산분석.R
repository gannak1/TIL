# 분산분석 (ANOVA)
# 총편차 = 처리내 편차 + 처리간 편차 
# (xij-x_bar) = (xij-xi_bar) + (xi_bar-x_bar)

# (주)한시경 온라인 강의 접속 시스템 속도 
# x1: pc, x2: 모바일, x3: 전용 어플리케이션

# 1. 데이터 입력 
x1 <- c(0.133,0.125,0.143,0.259,0.158,0.167,0.262,0.238,0.229)
x2 <- c(0.017,0.031,0.031,0.039,0.027,0.028,0.056,0.018,0.016)
x3 <- c(0.051,0.063,0.071,0.081,0.089,0.078,0.091,0.077,0.075)

# 2. 각 수준별 평균 구하기 
x1.mean <- mean(x1)
x2.mean <- mean(x2)
x3.mean <- mean(x3)

# 3. 처리 내 제곱합 구하기 
sse.1 <- sum( (x1-x1.mean)^2)
sse.2 <- sum( (x2-x2.mean)^2)
sse.3 <- sum( (x3-x3.mean)^2)

sse <- sse.1+sse.2+sse.3
sse

# 4. 처리 내 제곱합의 자유도 
dfe <- (length(x1)-1) + (length(x2)-1) + (length(x3)-1) 
dfe

# 5. 처리 간 제곱합 구하기 
x.mean <- (x1.mean + x2.mean + x3.mean )/3  #총평균

sst.1 <- length(x1)*sum((x1.mean-x.mean)^2) # n1*(x1.mean-x.mean)^2
sst.2 <- length(x2)*sum((x2.mean-x.mean)^2) # n2*(x2.mean-x.mean)^2
sst.3 <- length(x3)*sum((x3.mean-x.mean)^2) # n3*(x3.mean-x.mean)^2
sst <- sst.1 + sst.2 + sst.3 
sst

# 6. 처리 간 제곱합 자유도 
# d.f = n-1

dft <- (3-1)
dft

# 7. 검정통계량 F 
# F = 집단간 / 집단 내 

f <- (sst/dft)/(sse/dfe)
f

# 8. 검정통계량 유의확률 구하기 
p.value <- 1 - pf(f, 2, 24)
p.value

# pf(vector, df1, df2)

# R aov()

# 1. 데이터 불러오기

data_anova <- read.csv("systemAnova.csv")
data_anova

str(data_anova)

# 2. 변수 system 명목변수 생성
data_anova <- transform(data_anova, f_system=factor(system))
data_anova
sapply(data_anova, class) #변수 확인 

# 3. aov() 함수 이용, 분산분석
# aov(종속변수 ~ 독립변수, data=dataset)

aov(respondTime ~ f_system, data=data_anova)
data_aov <- aov(respondTime ~ f_system, data=data_anova)
summary(data_aov)

# 4. 다중비교 (Multiple Comparision)
# 어느 그룹에서 차이가 나는지 확인하기 위함 

# 1) Tukey's HSD 

TukeyHSD(data_aov) 

'''
$f_system
          diff        lwr        upr p adj
2-1 -0.1590778 -0.1974909 -0.1206647 1e-07

2-1 : 그룹2-그룹1
diff: 그룹2의 평균 - 그룹1의 평균 (-0.1590)
lwr : (그룹2의 평균 - 그룹1의 평균) 하한 (-0.1974)
upr : (그룹2의 평균 - 그룹1의 평균) 상한 (-0.1206)
p adj: 0.000
'''

# 2) Duncan's LSR 다중비교 
install.packages("agricolae")
library(agricolae)

duncan.test(data_aov, "f_system", alpha = 0.05, console=T)
# 요인변수 : f_system 지정, 유의순준 alpha=0.05
# console=T : 콘솔 창에 표시 

'''
Means with the same letter are not significantly different.
같은 글자로 써진 그룹은 유의수준 0.05에서 유의하게 차이가 나지 않음

결과: 그룹1,2 모두 차이가 난다. 


'''

# 5. 시스템 별 박스플롯 작성하기 
boxplot(respondTime ~ system, data=data_anova)
