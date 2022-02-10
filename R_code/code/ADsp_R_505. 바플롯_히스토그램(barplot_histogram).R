# barplot 이산형 데이터에 사용 
dev.off()
x <- c(1,2,3,4,5)
y <- c(6,7,8,9,10)

barplot(x)

barplot(x,horiz = T)

# Histogram 연속형 데이터 사용 

# set working directory
# change working directory 

# Read data
brain<-read.csv(file="brain.csv")

head(brain)
dim(brain)
str(brain)

attach(brain)
# attach(data)

# 1. histogram 

# 1-1. histogram with no options    
hist(brain$wt)
hist(wt)

help(hist)

hist(wt, col = "lightblue")

# 1-2. histogram with color and title, legend
# hist(변수이름, breaks="원하는 간격", col="colname", main="")

hist(wt, breaks = 10, col = "lightblue", main="Histogram of Brain weight" , xlab="brain weight")

stem(wt, scale=1)
boxplot(wt)

# see rgb values for 657 colors, choose what you like
colors()

# select colors including "blue" 
# grep("단어",colors(), value=TRUE): 단어가 포함된 색을 검색해 줌 

grep("violet", colors(), value=TRUE)

# 1-3. 밀도함수 그리기 fit function (find density function)
par(mfrow=c(1,1))
# 한 개의 창에 하나의 그림만 넣겠다는 의미 

d <- density(brain$wt)
plot(d)
