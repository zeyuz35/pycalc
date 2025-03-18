# Re-implementation of Machine Learning for Finance Code in Python
# Maybe using the Python libraries will make this better...

# preliminary
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Global Parameters
# Number of stocks
bigN = 200
# Number of Time Periods
bigT = 100
# Number of Characteristics that underly true model
P_c = 100

# Simulate the Characteristics

# rho ~ unif(a, b), constant across all times and stocks

# Inputs
# rho_a
# rho_b
# burn = 100, burn in period

# Outputs
# C_bar = bigN x P_c x bigT array of characteristics

def gen_C_bar(rho_a, rho_b, burn = 100):
    # initialze empty array
    P_c = numpy.zeros((bigN, P_c, bigT))


    return np.random.uniform(0, 1, P_c)




