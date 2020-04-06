import numpy as np
import gsfio 
import matplotlib.pyplot as plt
from scalebars import *
import scipy.signal as sgn
from scipy.optimize import curve_fit
from random import randint
import seaborn as sb

def fit_func(x,a,tau,y0):
    
    return (1.-a*np.exp(-x/tau))+y0

datadir="../Data"
dt=0.05

def do_bootstrap(fname,nBs=5):
    
    
    input_file=tuple(open(fname))
    x=[]
    y=[]

    for i in range(len(input_file)):
        line=input_file[i].split()
    
        for k in range(1,len(line)):
            x.append(float(line[0]))
            y.append(float(line[k]))
    
    
    bs_result=np.zeros(nBs)
    ns=0
    N=len(x)
 
    while ns<nBs:
        xBs=[]
        yBs=[]
        for i in range(0,N):
            k=randint(0,N-1)
            xBs.append(x[k])
            yBs.append(y[k])
        
        #try:
        popt,pcov=curve_fit(fit_func,np.array(xBs),np.array(yBs),(1,50,0))
            
        bs_result[ns]=popt[1]
        ns=ns+1
        #except:
         #   pass
    
    
    return bs_result

WT_KSCN_bs=do_bootstrap("WT_KSCN.txt")
WT_NASCN_bs=do_bootstrap("WT_NaSCN.txt")
MUT_KSCN_bs=do_bootstrap("L46P_KSCN.txt")
MUT_NASCN_bs=do_bootstrap("L46P_NaSCN.txt")

plt.figure()
sb.distplot((WT_KSCN_bs),color="r")
sb.distplot((WT_NASCN_bs),color="tomato")
sb.distplot((MUT_KSCN_bs),color="b")
sb.distplot((MUT_NASCN_bs),color="steelblue")
plt.savefig("All PPR Histogram.svg")
plt.show()

print np.mean(WT_KSCN_bs),np.std(WT_KSCN_bs)
print np.mean(WT_NASCN_bs),np.std(WT_NASCN_bs)
print np.mean(MUT_KSCN_bs),np.std(MUT_KSCN_bs)
print np.mean(MUT_NASCN_bs),np.std(MUT_NASCN_bs)

print 1-(WT_KSCN_bs > np.mean(MUT_KSCN_bs)).sum()/50000.

