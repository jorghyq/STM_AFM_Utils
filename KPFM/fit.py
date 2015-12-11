import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import re

def fit_freq(file_path,begin=None,end=None,ERROR_OUT=False):
    if os.path.isfile(file_path):
        with open(file_path) as f:
            temp = f.readlines()
        header = 0
        #print temp
        for line in temp:
            #print line
            match = re.search(r'DATA',line)
            #print match
            if match:
                header = header + 1
                break
            else:
                header = header + 1
            #print header
        #print 'header', header
        data = pd.read_csv(file_path,sep='\t',skiprows=header)
        bias = data['Bias calc (V)']
        freq = data['Frequency Shift (Hz)']
        data_size = bias.size
        #print data_size
        if begin == None:
            begin = 0
        if end == None:
            end = data_size
        #print begin, end
        z = np.polyfit(bias[begin:end], freq[begin:end], 2)
        x0 = -z[1]/(2*z[0])
        if ERROR_OUT:
            freq_fit = bias*bias*z[0]+bias*z[1]+z[2]
            error = abs(freq_fit[begin:end]-freq[begin:end]).sum()/(end-begin)
            return z,x0,error
        else:
            return z,x0


if __name__ == '__main__':
    file_path = './test/KPFM013.dat'
    z,x0,e = fit_freq(file_path,None,None,1)
    print z,x0,e
