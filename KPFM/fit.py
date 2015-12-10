import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import re

def fit_freq(file_path,begin=None,end=None):
    if os.path.isfile(file_path):
        with open(file_path) as f:
            temp = f.readlines()
        header = 0
        print temp
        for line in temp:
            print line
            match = re.search(r'DATA',line)
            print match
            if match:
                header = header + 1
                break
            else:
                header = header + 1
            print header
        print 'header', header
        data = pd.read_csv(file_path,sep='\t',skiprows=header)
        bias = data['Bias calc (V)']
        freq = data['Frequency Shift (Hz)']
        data_size = bias.size
        print data_size
        if begin == None:
            begin = 0
        if end == None:
            end = data_size
        print begin, end
        z = np.polyfit(bias[begin:end], freq[begin:end], 2)
        return z


if __name__ == '__main__':
    file_path = './test/KPFM013.dat'
    z = fit_freq(file_path,None,None)
