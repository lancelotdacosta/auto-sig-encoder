"""
Script orchestrating running of sig compression of data and its inversion using algo in
"Inverting the signature of a path", https://arxiv.org/abs/1406.7833
"""

# Build-ins import
import os, sys, inspect
import pandas as pd
import matplotlib.pyplot as plt

# Home-brew import
import iisignature
from pprint import pprint
import seaborn as sns

# (importing our modules)
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
package_dir = os.path.dirname(current_dir).replace("run_files", "") + "/src"
sys.path.insert(0, package_dir)
import base.sig_computer
import base.inverse_sig_computer
import base.auto_encoders
from data.data_preparation import data_set_1


# 1. setting auto-encoder
pass

# 2. Transforming data into signature
sig = iisignature.sig(handwritting_ds.training_X_ordered[1], 3)
handwritting_ds = data_set_1()

# 3. Start training
