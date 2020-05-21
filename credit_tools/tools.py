import numpy as np
from pandas.core.series import Series

def standardize(x: Series, with_plot: bool = False) -> Series:
    """표준화 
    
    - 설명 
        - 평균을 기준으로 얼마나 떨어져 있는지를 나타내는 값
        - 2개 이상의 대상이 단위가 다를 때 데이터를 같은 기준으로 볼 수 있게 한다.  
        - 평균을 0으로 표준편차를 1로 만들어 준다.
        
    - TODO
        - with_plot 변수가 동작하도록 할 것
    
    Args:
        x(Series): 표준화 될 대상
        with_plot(bool): 표준화 된 x의 그래프를 그릴지 여부
    """
    return (x - np.mean(x) / np.std(x))


def covariance(var1, var2, bias=0):
    """
    
    """
    observations = float(len(var1))
    return np.sum((var1 - np.mean(var1)) * (var2 - np.mean(var2))) / (observations - min(bias, 1))

def correlation(var1, var2, bias=0):
    """
    
    """
    return covariance(standardize(var1), standardize(var2), bias) / (np.std(var1) * np.std(var2))