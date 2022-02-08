install.packages("MASS")
library(MASS)

data(eurodist)
str(eurodist)
eurodist

# 계량적 다차원 척도법(cmdscale()함수 사용) 수행
MDSEurodist <- cmdscale(eurodist)

MDSEurodist

plot(MDSEurodist) 

text(MDSEurodist, rownames(MDSEurodist), cex=0.7, col="red")

abline(v=0, h=0, lty=1, lwd=0.5)
# abline(): 그림에 중앙선 그려 상대적 거리 비교 

#비계량적 다차원 척도법 실습 
install.packages("HSAUR")
library(HSAUR)

# 데이터 읽기
# 15명의 의원이 19개 환경 법안에 투표한 결과 데이터 
data("voting", package= "HSAUR")
library(MASS)
voting 
head(voting)
str(voting)

# Hunt와 sandman이 만나는 값 8의 의미: 19개 법안 중 8개 법안 투표
# 제출된 법안에 대한 의원들의 성향 나타냄 

MDSvoting <- isoMDS(voting)  
# 비계량 다차원 척도법(isoMDS()) 수행 

MDSvoting  

# 그래프로 표현
x <- MDSvoting$point[,1]
y <- MDSvoting$point[,2]

plot(x,y) # 점(point)로 표현

text(x, y, labels= colnames(voting))
