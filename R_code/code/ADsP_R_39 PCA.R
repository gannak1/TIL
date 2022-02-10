# 주성분 분석(Principal Component Analysis)
data("USArrests")
str(USArrests)
nrow(USArrests)
rownames(USArrests)

apply(USArrests, 2, var)

# prcomp() 주성분 분석 수행

USArrests_pca<-prcomp(USArrests, center=T, scale=T)
# 주성분 분석 수행(평균=0 center=T, 분산=1 scale=T) 설정

names(USArrests_pca)

summary(USArrests_pca)

print(USArrests_pca)
# PC1 
# (-0.5358995)*Murder+(-0.5831836)*Assault*(-0.2781909)*UrbanPop*(-0.5434321)*Rape

plot(USArrests_pca, type="l")

# 직교회전한 그래프
biplot(USArrests_pca)






