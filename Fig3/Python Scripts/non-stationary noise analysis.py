import numpy as np
import gsfio 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib import gridspec
from random import randint
import seaborn as sb


def fit_func(I,i,N):
    
    return i-I/float(N)

datadir="../Data"

Zellen=['/2016_07_06/2016_07_06_10.dat', '/2016_07_06/2016_07_06_12.dat', '/2016_07_07/2016_07_07_2.dat', '/2016_07_08/2016_07_08_1.dat', '/2016_07_08/2016_07_08_2.dat', '/2016_07_08/2016_07_08_4.dat', '/2016_07_13/2016_07_13_2.dat', '/2016_07_13/2016_07_13_4.dat', '/2016_08_02/2016_08_02_z5.dat', '/2016_08_02/2016_08_02_z6.dat', '/2016_08_03/2016_08_03_z4.dat','/2016_08_16/2016_08_16_z7.dat', '/2016_08_16/2016_08_16_z8.dat', '/2016_08_17/2016_08_17_z4.dat', '/2016_08_17/2016_08_17_z5.dat', '/2016_08_17/2016_08_17_z7.dat', '/2016_08_17/2016_08_17_z9.dat']

Zellen2=['/2016_07_14/2016_07_14_1.dat', '/2016_07_14/2016_07_14_7.dat', '/2016_08_04/2016_08_04_z2.dat', '/2016_08_04/2016_08_04_z6.dat', '/2016_08_04/2016_08_04_z10.dat', '/2016_08_05/2016_08_05_z1.dat']

def read_data(Zelle,start=2500,ende=3900):
    
    try:
        dat=gsfio.loadPatchmasterFile2(datadir+Zelle)
    except:
        print Zelle
    noises=[]
    for i in range(len(dat)):
        if len(dat[i])>=300:
            noise_rec = -np.array(dat[i],dtype='float64')
            break
   
    Imean = np.mean(noise_rec,axis=0)
    Idiff = np.diff(noise_rec,axis=0)
    var_Idiff = np.var(Idiff,axis=1)
    thres=2.0

    ind_sorted = np.argsort(var_Idiff)
    ind_keep = ind_sorted[:-int(len(ind_sorted)*0.1)]
    variance=np.mean((Idiff[ind_keep]**2),axis=0)/2.

    Imax=np.max(Imean[start:ende])
    Inorm=Imean[start:ende]/Imax
    sigma_bg=np.mean(variance[0:100])
    
    bins=[]
    Imin=np.min(Imean[start:ende])
    Imax=np.max(Imean[start:ende])
    for j in range(0,51):
        bins.append(Imin+j*(Imax-Imin)/50)
    binindex=np.digitize(Imean[start:ende],bins)
    I_bin_means = [Imean[start:ende][binindex == k].mean() for k in range(1, len(bins))]
    sigma_bin_means=[variance[start:ende][binindex == k].mean() for k in range(1, len(bins))]
    I_bin_norm=I_bin_means/np.max(I_bin_means)

    
    return Imean[start:ende],Idiff[start:ende],variance[start:ende],Inorm,sigma_bg,I_bin_means,sigma_bin_means,I_bin_norm
    
    
    

def do_noise(Zelle):
   
    
    data=read_data(Zelle)
    I_bin_means=data[5]
    variance=data[2]
    sigma_bin_means=data[6]
    sigma_bg=data[4]
    try:
        popt,pcov=curve_fit(fit_func,I_bin_means,(sigma_bin_means-sigma_bg)/I_bin_means)
        i,N=popt[0],popt[1]
    except:
        print Zelle
        i=-1
        N=1e15

    return i,N
    
def plot_all_in_one(Zellen,Zellen2=[]):
    
    
    
    plt.figure()
    allx=[]
    ally=[]
    
    allx2=[]
    ally2=[]
    for Zelle in Zellen:

        data=read_data(Zelle)
        sigma=data[6]
        sigma_bg=data[4]
        
        Inorm=data[7]  
        Imean=data[5]
        plt.plot(Inorm,((sigma-sigma_bg)*1000)/Imean,"o",color="b")
        plt.xlim((0,1.4))
 
        allx=allx+list(Inorm)
        ally=ally+list((sigma-sigma_bg)/Imean)
 
    try:
        popt,pcov=curve_fit(fit_func,np.array(allx),np.array(ally)*1000,(0.03,0.02))
        x=np.linspace(0,1.4,100)
    except:
        pass
   
    plt.plot(x,fit_func(x,popt[0],popt[1]),color="b")
    for Zelle in Zellen2:

        data=read_data(Zelle)
        sigma=data[6]
        sigma_bg=data[4]
        
        Inorm=data[7]  
        Imean=data[5]
      
        plt.plot(Inorm,((sigma-sigma_bg)*1000)/Imean,"o",color="r")
        plt.xlim((0,1.4))
        
        allx2=allx2+list(Inorm)
        
        ally2=ally2+list((sigma-sigma_bg)/Imean)
 
    try:
        popt2,pcov2=curve_fit(fit_func,np.array(allx2),np.array(ally2)*1000,(0.03,0.02))
        x2=np.linspace(0,1.4,100)
        
    except:
        pass

    
    plt.xlabel("norm. I/Imax")
    plt.ylabel("$\Delta$ Variance/I (fA)")
    plt.ylim(-5,60)
    plt.xlim(0,1.4)
    
    if Zellen2!=[]:
        plt.plot(x,fit_func(x,popt2[0],popt2[1]),color="r")
    plt.savefig("Noise_NaNO3.svg")
    plt.show()


def plot_raw_data(Zelle):
    
    data=read_data(Zelle)
    plt.figure()
    plt.plot(data[0])
    plt.plot(data[2])
   
    plt.show()
    
def plot_raw_data_full(Zelle):
    
    data=read_data(Zelle,0,5400)
    plt.figure()
    plt.plot(data[0])
    #plt.plot(data[2])
    plt.ylim( (-1500,2500) )
    plt.xlim(1500,5500)
    plt.xlabel("Timepoint")
    plt.ylabel("I (pA)")
    plt.show()
    
    
    
def find_good_ones(Zellen):
    current_cells=[]

    for Zelle in Zellen:
        data=read_data(Zelle)
    
        if np.max(data[2])-data[4]<40 or np.max(data[2])-data[4]>500:
            continue
        if do_noise(Zelle)[1]<1e6:
            current_cells.append(Zelle)
    return current_cells



def read_norm_data_all(Zellen):
    

    allx=[]
    ally=[]
    

    for Zelle in Zellen:
        #print Zelle
        data=read_data(Zelle)
        sigma=data[6]
        sigma_bg=data[4]
        
        Inorm=data[7]
        
        Imean=data[5]
      
       
        
        allx=allx+list(Inorm)
        
        ally=ally+list((sigma-sigma_bg)/Imean)
        
    return allx,ally

def do_bootstrap(Zellen,nBs=50000):
    
    
    bs_result=np.zeros(nBs)
    ns=0
    
    x,y=read_norm_data_all(Zellen)
    N=len(x)
    
    while ns<nBs:
        xBs=[]
        yBs=[]
        for i in range(0,N):
            k=randint(0,N-1)
            xBs.append(x[k])
            yBs.append(y[k])
        
        try:
            popt,pcov=curve_fit(fit_func,np.array(xBs),np.array(yBs),(0.03,0.02))
            
            bs_result[ns]=popt[0]
            ns=ns+1
        except:
            pass
    
    
    return bs_result
        
            
        

MUT_bs=do_bootstrap(Zellen,50000)
WT_bs=do_bootstrap(Zellen2,50000)
np.savetxt("WT_bsres.txt",np.array(WT_bs))
np.savetxt("MUT_bsres.txt",np.array(MUT_bs))


plt.figure()
sb.distplot(WT_bs*1000,color="r")
sb.distplot(MUT_bs*1000)
plt.savefig("Histogram.svg")
plt.show()

print np.mean(WT_bs),np.std(WT_bs)
print np.mean(MUT_bs),np.std(MUT_bs)
print (WT_bs > np.mean(MUT_bs)).sum()/50000.
print MUT_bs[0:5]

plot_all_in_one(Zellen,Zellen2)


