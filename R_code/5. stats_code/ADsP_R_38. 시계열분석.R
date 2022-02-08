# 시계열분석

# 시계열 데이터 생성

a <- ts(1:30, frequency=12, start=c(2017.1)) 
# 시계열 데이터로 변형하는 명령어 ts

a
# 만들어진 데이터가 시계열 데이터로 변형되었는지 확인

attributes(a)
# 데이터 속성 보여줌 

aa <- ts(1:24, start=2010, end=2012, frequency=12)  
# 시계열 데이터로 변경

aa                           
attributes(aa)

# 시계열 데이터 분해 단계

AirPassengers
# 1949~1960년 사이 비행기 승객 수 데이터

plot(AirPassengers)
# 데이터 파악 위한 시각화 

apts <- ts(AirPassengers, frequency=12)  
# 분석 위해 데이터 변형(시계열 데이터로 변환)

f <- decompose(apts)  
# 변환된 데이터 분해(decompose(): 시계열 데이터 분해)

f     
# 트렌드 변동(trend): 시간의 흐름에 대한 변동
# 계절변동(seasonal): 계절에 대한 변동요인
# 우연적변동(random): 우연히 일어난 변동

plot(f)   

#그래프 구성 및 결과 해석
# 1번째: 원 시계열 데이터
# 2번째(trend): 전체 데이터 흐름
# 3번째(seasonal): 계절적 요인에 대한 변동
# 4번째(random): 기타요인 
# figure : 1주기(여기서는 1년)

# 결과해석: trend만 변화 보임

plot(f$figure, type="b", xaxt="n", xlab="") 
# f 결과의 figure 내용을 그래프로 표현

monthNames <- months(ISOdate(2019, 1:12, 1))
# 표현된 그래프에 월 이름 부여(ISOdate():ISO 스타일로 날짜 나타냄)

axis(1, at=1:12, labels=monthNames, las=2)

# 그림 결과 해석
# 1년 주기로 분석하면, 7-8월이 성수기, 11월이 비수기 (승객수 저조)

# 시계열 데이터 변환 단계

install.packages("tseries") 
library(tseries)

adf.test(diff(log(AirPassengers)), alternative="stationary", k=0)
# AirPassengers 데이터에 로그취한 뒤 차분(diff)하여 변환
# adf.test(): 주어진 데이터 변환, diff(): 빼는 과정 수행 

# 결과해석
# p-value = 0.01 < 0.05 : 안정적으로 판단 

# 파라이터 최적화
library(forecast)

par(mfrow=c(2,1))

#ACF/PACF 분석 차트 그리기 
acf(diff(log(AirPassengers)))  # MA 모델
pacf(diff(log(AirPassengers))) # AR 모델

#acf(): ACF 분석(이동평균모델(MA:Moving Average))모델 평가 위한 분석 
#pacf(): PACF 분석(자귀회귀이동평균모델(Auto Regressive Moving Average))
#모델 평가 위한 분석

# ARIMA 모델(**)
auto.arima(diff(log(AirPassengers)))
#auto.arima(): ARIMA 모델 파라미터 얻기 위함 

# 예측모델에 사용할 파라미터 활용
# ARIMA(0,0,1)(0,1,1)

install.packages("ggfortify")
library(ggfortify)

tsdiag(auto.arima(diff(log(AirPassengers))))
#tsdiag(): auto.arima 분석결과 시각화 

# 그림분석 결과 해석
# ARIMA 필요한  파라미터가 모형의 가정 만족 여부 확인
# 1번째(standardized Residuals): 특정 패턴(증가,감소,반복) 발견 못함
# 2번째(ACF of Residuals): 지속적 감소 경향 
# 3번째(p value): 점선 위에 있음
# 여기서는 필요 조건 만족 
# ARIMA 모델 
# p(AR모델의 차수), d(트렌드 제거 후 안전 시계열로 만들기 위한 차수)
# q(MA의 차수) 

# 모형 만들기와 예측 단계

# 모형 적합 
fit <- arima(log(AirPassengers), c(0,0,1), 
             seasonal=list(order=c(0,1,1),period=12)) 
# 최적 파라미터로 얻은 ARIMA(0,0,1)(0,1,1) 사용 

# 예측 
autoplot(forecast(fit))

# 시계열 분석 self-study

ldeaths # 폐질환 사망자에 관한 자료(1974~1979년)
plot(ldeaths)

# decompose() 함수: 시계열 자료를 4가지 요인으로 분해 하는 함수    
ldeaths.decomp<-decompose(ldeaths)
ldeaths.decomp$seasonal

plot(ldeaths.decomp)

ldeaths.decomp.adj<-ldeaths - ldeaths.decomp$seasonal
plot(ldeaths.decomp.adj)


