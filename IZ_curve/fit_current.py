import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import re

def fit_current(file_path,begin=None,end=None,BACKWARD=False,ERROR_OUT=False):
    if os.path.isfile(file_path):
        with open(file_path) as f:
            temp = f.readlines()
        header = 0
        #print temp
        for line in temp:
            #print line
            match = re.search(r'DATA',line)
            #print match
            match_height = re.search(r'Z \(m\)',line)
            #print line
            if match_height:
                #print line.split('\t')
                #print line.split('\t')[-2].strip()
                z_set = float(line.split('\t')[-2].strip())
                #print z_set
            if match:
                header = header + 1
                break
            else:
                header = header + 1
            #print header
        #print 'header', header
        data = pd.read_csv(file_path,sep='\t',skiprows=header)
        height = data['Z (m)']#*1e10
        if BACKWARD:
            current = data['Current [bwd] (A)']#*1e9
        else:
            current = data['Current (A)']#*1e9
        data_size = height.size
        #print data_size
        if begin == None:
            begin = 0
        if end == None:
            end = data_size
        #print begin, end
        # compute log
        log_current = np.log(abs(current))
        z = np.polyfit(height[begin:end], log_current[begin:end], 1)
        x0 = z[0]*z[0]*(9.525e-21)
        if ERROR_OUT:
            current_fit = height*z[0]+z[1]
            error = abs(current_fit[begin:end]-log_current[begin:end]).sum()/(end-begin)
            return z,x0,error,z_set
        else:
            return z,x0,z_set


if __name__ == '__main__':
    file_path = './test/Z-Spectroscopy_grid1_261.dat'
    z,x0,e,z_set = fit_current(file_path,None,None,0,1)
    print z,x0,e,z_set
