
setwd("G:\\R\\R_basic\\R_basic_startR\\data")

setwd("C:\\Users\\ppos7\\OneDrive\\바탕 화면\\인프런_ADsP\\1.R 기초_code")

#read.csv("aa")
x<-read.csv("aa.csv")
x

y<-read.csv("bb.csv")
y

y<-read.csv("bb.csv", header=FALSE)
y


names(y) <- c("id","name","score")
y


write.csv(y, "cc.csv", row.names=FALSE) 

y<-read.csv("cc.csv")
y

# text file 을 읽을 때
txt<-read.table("houses.txt", header=T)
txt

write.csv(txt,"dd.csv", row.names = FALSE)


