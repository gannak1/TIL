# 데이터 정규성 검정
# Normality test, confidence interval

# set working directory
getwd()

### student math grade data ####

stud<-read.csv("stud_math.csv", stringsAsFactors = TRUE)

head(stud)
dim(stud)
str(stud)

attach(stud)
dev.off()
# 1-2 Testing for normality
#Quantile plot
qqnorm(G1)
qqline(G1, col = 2, cex=7)
#qqline의 default는 정규분포의 1Q,3Q 직선

qqnorm(G2)
qqline(G2, col = 2, cex=7)

qqnorm(G3)
qqline(G3, col = 2, cex=7)


#정규분포 적합성 검정
# - 데이터가 정규분포 하는지에 대한 검정

#Shapiro-Wilks test
shapiro.test(G3)

'''
 
	Shapiro-Wilk normality test

data:  G3
W = 0.92873, p-value = 8.836e-13

결과 해석 
- G3는 정규분포한다고 말할 수 없다.
- p-value가 거의 0 에 가까움

'''

#Anderson-Darling test require installing package "nortest"
install.packages('nortest')
library(nortest)
ad.test(G3)

'''

Anderson-Darling normality test

data:  G3
A = 8.3032, p-value < 2.2e-16

결과 해석 
- G3는 정규분포한다고 말할 수 없다.
- p-value가 거의 0 에 가까움

'''

# data simulation
# Simulation examples
runif(5,min=1,max=5)   # random, uniform distribution
rnorm(5,mean=5,sd=1)   # random, normal distribution
rbinom(5,size=100,prob=.2) #ramdp,binomial distribution

# 정규분포 normal distribution
x<-rnorm(1000)
plot(density(x),xlim=c(-5,10))

# random seed 10
set.seed(10)
# 1000개의 데이터를 정규분포에서 생성하여 얻은 평균값 
mean(rnorm(1000))
# 0.016

