# This script is reading in line scan and shows out
# 0. line scan shifted in z direction
# 1. 2D map with each x-row as a line scan

import os
import numpy

def view_linescan(file_path,maching_name,output_path,mode=0):
    if os.path.exists(file_path):
        files = os.listdir(file_path)

