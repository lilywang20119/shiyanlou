import pandas as pd
import datetime

def quarter_volume():
    data = pd.read_csv('apple.csv',header=0)
    s = data.Date
    s = s.to_