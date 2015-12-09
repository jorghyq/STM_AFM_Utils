import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

def fit_freq(file_path,begin,end):
    if os.path.isfile(file_path):
        data = pd.read_csv(file_path,sep='\t',skiprows=22)
        bias = data['Bias calc (V)']
        freq = data['Frequency Shift (Hz)']
        z = np.polyfit(bias[begin:end], freq[begin:end], 2)
        return z
