# plot(산점도)

# 자료구조 확인
str(cars)
cars$speed
cars$dist

plot(cars$speed, cars$dist, main="속도와 제동거리", xlab="속도(mph)", ylab="제동거리(ft)", pch=1, col="red")
plot(cars$speed, cars$dist, main="속도와 제동거리", xlab="속도(mph)", ylab="제동거리(ft)", pch=2, col="blue")

Nile
str(Nile)

plot(Nile, main="Nile강의 연도별 유량 변화", xlab="연도", ylab="유량")
plot(Nile, type="p", main="Nile강의 연도별 유량 변화", xlab="연도", ylab="유량")
plot(Nile, type="l", main="Nile강의 연도별 유량 변화", xlab="연도", ylab="유량")
# pch: point character (점의 형태), type = p (points) , type = l (lines)