
kimchi.pivot_table(index = '판매월',   # index 방향에 배치할 컬럼명
                   columns = '판매처', # columns 방향에 배치할 컬럼명
                   values = '수량',   # 교차표에 작성할 값을 갖는 컬럼명 
                   aggfunc = 'sum'   # 그룹 함수
                   )