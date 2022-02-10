# 두 그룹간 평균차이분석(T-test)
# t-test for two sample means

# set working directory

### student math grade data ####
stud<-read.csv("stud_math.csv", stringsAsFactors = TRUE)

head(stud)
dim(stud)
str(stud)

attach(stud)

# 1. single t-test : 
# to test whether or not mean of G3 is 10
# H0 : G3(최종성적)의 평균은 10이다

t.test(G3, mu=10)

'''
One Sample t-test

data:  G3
t = 1.8011, df = 394, p-value = 0.07245
alternative hypothesis: true mean is not equal to 10
95 percent confidence interval:
  9.961992 10.868388
sample estimates:
mean of x 
 10.41519 

Ha(대립가설) : 모 평균은 10이 아니다 

결론 : alpha = 0.05에서 G3 평균이 10이라고 할 수 있음
     - p-value = 0.07245 > 0.05(alpha)
'''

# 2. two sample t-test
# - to test whether or not mean of G3 
# is same between Urban and Rural 
# H0 : 거주지역(R,U)에 따른 G3(최종성적) 평균에 차이가 있는가? 

t.test(G3~address, data=stud)
boxplot(G3~address, boxwex = 0.5, col = c("yellow", "coral"))

'''
	Welch Two Sample t-test

data:  G3 by address
t = -2.1101, df = 140.91, p-value = 0.03661
alternative hypothesis: true difference in means between group R and group U is not equal to 0
95 percent confidence interval:
 -2.25240320 -0.07340373
sample estimates:
mean in group R mean in group U 
       9.511364       10.674267 
       
결론 
- p-value = 0.03661 < 0.05(alpha)
- 유의수준 0.05에서 거주지역에 따라 G3 유의한 차이가 있음 

'''

help(t.test)

## example 2 
# to test whether or not mean of G3 
# is equal for activities 

# H0 : 방과후 활동여부(YES, NO)에 따른 G3(최종성적) 평균에 차이는 없다
t.test(G3~activities, data=stud)
boxplot(G3~activities, boxwex = 0.5, col = c("blue", "red"))


'''

	Welch Two Sample t-test

data:  G3 by activities
t = -0.31944, df = 392.98, p-value = 0.7496
alternative hypothesis: true difference in means between group no and group yes is not equal to 0
95 percent confidence interval:
 -1.0542623  0.7595503
sample estimates:
 mean in group no mean in group yes 
         10.34021          10.48756
         
결론 : 뚜렷한 차이가 없음 
- p-value = 0.7496 > 유의수준(alpha) 0.05 
- boxplot 비교시 차이가 없음 
'''

# 3. 비모수적 방법(Non-parametric method)
# Wilcoxon signed-rank test

# wilcox.test(G3, mu=10)
wilcox.test(G3~address)

'''
Wilcoxon rank sum test with continuity correction

data:  G3 by address
W = 11278, p-value = 0.01776
alternative hypothesis: true location shift is not equal to 0

결론 
- p-value = 0.01776 < 0.05 
- 거주지역에 따른 학업성적에 유의한 영향을 줌

'''

# [연습문제]
t.test(G3~internet, data=stud) 


help(wilcox.test)

