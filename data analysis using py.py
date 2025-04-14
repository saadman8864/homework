import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# Specify the delimiter and error handling
df = pd.read_csv('https://www.kaggle.com/datasets/ak0212/uae-cancer-patient-dataset', encoding='latin-1', delimiter='\t', on_bad_lines='skip')
# If the delimiter is not a tab, try other common delimiters like semicolon (;) or pipe (|)

df.head()
