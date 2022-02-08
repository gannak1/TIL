# Hypothesis Testing (가설검정)

# Distributions (분포)
# a function showing the possible values 
# for a variable and how often they occur

# normal distribution = probability distribution 
# (정규분포, 확률적 분포, 확률밀도함수)
# 1) perfectly symmetrical (완전대칭)
# 2) most probable values are around the mean (평균 중심)

# z-score (z)
# standardized variable (z) 
# z = (origianl variable - mean) / sd(standard deviation)

# standard error and confidence intervals
# 표준오차, 신뢰구간 

# standard error(표준오차)
# standard deviation : a measure of variability 
# standard error: a measure of variability on a larger scale 

# population(모집단) vs. sample(표본) 
# 모집단 평균 : mu, 표본집단 평균: x_bar

# more samples, more sample means
# their average is closer to the population mean 
# If you have a sample with over 30 observations, 
# you can accept that the sampling distribution with mean 
# equals to the population mean 

# so, standard error means
# sd of sample error 
# sd gives us the level of certainty 
# with which we can generalize 
# from a sample to a population 

# confidence level (신뢰구간)
# a range of values where the poplulation mean is likely to fall
# (lower boundary, upper boundary) e.g. x_bar - 2, x_bar + 2

# Steps in data-driven decision making
# 데이터에 근거한 의사결정

# 1. Research question 목적 
# 2. Generate a theory 이론적 지식 접목 
# 3. Formulate a hypothesis 가설설정 
# 4. Find correct test 적합한 테스트 
# 5. Execute the test  테스트결과 해석
# 6. Make a decision   의사결정 

# Hypothesis (가설)
# A hypothesis is a statement that can be tested

# H0(The null hypothesis) 영가설 
# what the theory predicts will be FALSE
# 70% of believers of Shin-Chun-Gi have caught Corona Virus.  
# H0: SCG_Mean(corona) = 70%
# Not prove but reject this!

# H1(Ha)(The alternative hypothesis) 대안가설, 연구가설 
# what the theory predicts will be TRUE
# 70% of believers of Shin-Chun-Gi don't have caught Corona Virus. 
# H1: SHG_Mean(corona) != 70%
# Not prove but support this!

# Type 1, Type 2 errors

# Type 1 error
# rejecting a true null (False Positive)
# H0(영가설) 사실인데 , 기각하는 경우 1-alpha
# probability: alpha

# Type 2 error
# accepting a false null (False Negative)
# H0(영가설) 틀렸는데, 승인하는 경우 1-beta (검정력)
# probability: beta

# z = (x-x_bar)/sqrt(sd)
# z ~ N(0,1)
# Standardization lets us compare the means

# sample mean: $100,200
# population sd: $15,000
# standard error: $2,739
# sample size: 30
# z-score: -4.67 
# H0 : $113,000
# two-sided test (양측검정)

sal <- read.csv("salary.csv")
summary(sal)
boxplot(sal)

z.test <- function(a, mu, sd){
  z = ((mean(a)-mu)/(sd/sqrt(length(a))))
  return(z)
}

z.test(a = sal$salary, mu=113000, sd=15000)
# -4.673765
# (-4.67) < (-z) --> 4.67 > z 
# The absoulte value of the z score should be higher
# than the absolute value of z 
# alpha(유의수준) = 0.05 (95% confidence level)
# z = 1.96, so, 4.67 > 1.96 
# therefore, the null is rejected
# H0 영가설은 기각, H1(Ha) 연구가설 지지 

# p-value : p-value() < 0.05: 통계적 유의  


