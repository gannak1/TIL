import numpy as np
import pandas as pd
from pandas import Series,DataFrame
a = Series([1,2,3,4],index=['a','b','c','d'])
b = Series([5,6,7,8],index=['e','f','g','h'])
a.add(b,fill_value=0)
a


1-1