# https://datascienceschool.net/02%20mathematics/05.02%20%EC%A0%9C%ED%95%9C%EC%A1%B0%EA%B1%B4%EC%9D%B4%20%EC%9E%88%EB%8A%94%20%EC%B5%9C%EC%A0%81%ED%99%94%20%EB%AC%B8%EC%A0%9C.html#id4
# SLSQP 알고리즘이 구현된 라이브러리를 통한 optimization
# SLSQP 알고리즘에 대한 공부는 차차 해야할듯..

import scipy as sp
import numpy as np

def fx(x):
    return np.sqrt((x[0] - 4) ** 2 + (x[1] - 2) ** 2)

# 제한 조건 상수
k = 1
def ieq_constraint(x):
    return np.atleast_1d(k - np.sum(np.abs(x)))


sp.optimize.fmin_slsqp(func=fx, x0=np.array([0, 0]), ieqcons=[ieq_constraint])