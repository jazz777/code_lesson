'''
inlineがきかない
colabでは動作する
'''
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

s=np.sin(np.pi*np.arange(0.0,2.0,0.01))
t=plt.plot(s)
