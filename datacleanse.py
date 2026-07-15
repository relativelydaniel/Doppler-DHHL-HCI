import numpy as np 
import pandas as pd

class DataCleaner: # pull from each data source in two classes
    def __init__(self):
        # initialuse ds1 - DHH annotations
        file = "General Lexicon DHH Annotations.tsv"
        df1 = pd.read_csv(file)
    
    def clean_data(self):
      
      # display dimensions of dataframe 
      print("\n Dimensions of dataframe")
      print(self.df.shape) 
      
      print("\nColumn names") 
      print(self.df.columns.tolist())
      
      # display first 15 rows 
      print("\n")
      print(self.df.head(15)) 
      
      print(self.df.info()) 
      
      # display count of missing values#
      print("\n Missing values count: ")
      print(self.df.isnull().sum().reset_index(name = 'Missing Values Counted')) # process and clean individually beforesyncing via merging / concatenating

  
