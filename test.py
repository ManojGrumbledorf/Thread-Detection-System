import pandas as pd
import numpy as np
import matplotlib
from sklearn import datasets

# Test libraries
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)
print("Matplotlib version:", matplotlib.__version__)  # Correct way to check Matplotlib version
iris = datasets.load_iris()
print("Scikit-learn loaded dataset:", iris['target_names'])
