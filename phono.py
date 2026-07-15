import numpy as np
import pandas as pd


# Mathematical engine Z/H's Law and core NLP
class PhonoEngine():
    def __init__(self, df1, df2): 
        if isinstance(df1, df2, pd.DataFrame):
                self.df = df1.merge(df2, how='right') # full join like merge
                print("DataFrame merged successfully.")
        else:
            df1 = pd.DataFrame(df1)
            df2 = pd.DataFrame(df2) 
            self.df = df1.merge(df2, how='right')
            print("DataFrame merged successfully.")