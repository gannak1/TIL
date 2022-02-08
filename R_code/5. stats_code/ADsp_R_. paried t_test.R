# 짝을 이루는 그룹 간 평균 비교

# paired t-test for two sample means

# set working directory

## example 1: blood pressure data
bp<-read.csv("bp.csv") 
attach(bp)

# paired t-test (two-sided) 양측검증 
# t.test(before, after, mu=0, paired=T)
t.test(bp_pre, bp_post, mu=0,  paired=T)
'''
Paired t-test

data:  bp_pre and bp_post
t = 4.5095, df = 9, p-value = 0.001469
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
  7.226228 21.773772
sample estimates:
mean of the differences 
                   14.5 

결론
- p-value = 0.001469 < 0.05(alpha)
- H0 기각, 투약 전과 투약 후 혈압에 유의한 차이가 있음
- 평균 14.5 만큼 혈압이 떨어짐


'''
# paired t-test (one-sided) 단측검정
t.test(bp_pre, bp_post, mu=0, alternative="greater", paired=T)

'''
Paired t-test

data:  bp_pre and bp_post
t = 4.5095, df = 9, p-value = 0.0007344
alternative hypothesis: true difference in means is greater than 0
95 percent confidence interval:
 8.605783      Inf
sample estimates:
mean of the differences 
                   14.5 

'''

## example 2: Very Low-calroie diet 극저 칼로리 식이요법 
diet<-read.csv("weight.csv") 
attach(diet)

# paired t-test (default=two-sided, 95% confidence interval)
t.test(wt_pre, wt_post, mu=0,  paired=T)

'''
Paired t-test

data:  wt_pre and wt_post
t = 12.74, df = 8, p-value = 1.357e-06
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 18.50003 26.67775
sample estimates:
mean of the differences 
               22.58889 
               
결론 
- 극저 칼로리 식이요법이 체중감량에 유의한 효과가 있다 

'''

# to get 90% confidence interval in paired t-test
t.test(wt_pre, wt_post, mu=0, alternative="two.sided", paired=T, conf.level=.90)








