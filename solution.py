import pandas as pd
import numpy as np


chat_id = 834639322 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    from statsmodels.stats.proportion import proportions_ztest

    p_val_0 = 0.02
    zstat, p_val_1 = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], 
                                       alternative='smaller')

    return p_val_1 < p_val_0
