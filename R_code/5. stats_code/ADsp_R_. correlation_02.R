# 상관분석
# 1. 피어슨 상관계수 

## 데이터 불러오기 
data = read.csv("correlation_example.csv", header=T)
head(data)
tail(data)

pairs(data)
### var2와 var3간 증가하는 관계 발견 

# 스피어만 상관 분석(서열)

cor(data, method="spearman")
