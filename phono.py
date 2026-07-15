import numpy as np
import pandas as pd


# Mathematical engine Z/H's Law and core NLP
class PhonoEngine():
    def __init__(self, ds1, ds2): 
        if isinstance(ds, ds2, pd.DataFrame):
                self.df = ds.merge(ds2, how='right') # full join like merge
                print("DataFrame merged successfully.")
        else:
            df1 = pd.DataFrame(ds)
            df2 = pd.DataFrame(ds2) 
            self.df = df1.merge(df2, how='right')
            print("DataFrame merged successfully.")