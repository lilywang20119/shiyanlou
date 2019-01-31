import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

s = Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
df = pd.DataFrame(np.random.rand(5,4),columns=['A','B','C','D'])

