#!/usr/bin/env python 
"""
lambda_noah40povis - a collection of Data Science helper functions 
"""

import pandas as pd 
import numpy as np 

from . import example_module 

TEST = pd.DataFrame(np.ones(10))
Y = example_module.increment(example_module.x)

