import pandas as pd
import numpy as np

def calculate_average(file, print_average):
    df = pd.read_csv(file)
    column_values = df["polysemy"].values
    average = np.mean(column_values)
    if print_average:
        print(average)





