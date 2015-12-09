import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

def fit_plot(file_path, PLOT, ERROR):
    if os.path.isfile(file_path):
        data = pd.read_csv(file_path,sep='\t',skiprows=22)
        bias = data['Bias calc (V)']
        freq = data['Frequency Shift (Hz)']
        z = np.polyfit(bias, freq, 2)
        fit = z[0] * bias * bias + z[1] * bias + z[2]
        error = sum(abs(freq - fit))
        if ERROR:
            return error
        if PLOT:
            plt.plot(bias, freq, 'o', bias, fit, 'r')
            plt.show()
