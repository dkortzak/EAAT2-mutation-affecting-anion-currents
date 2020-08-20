import numpy as np
import gsfio 
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import stfio
from scipy.optimize import curve_fit
import scipy
from scalebars import *
from scipy import stats

Vs0=np.linspace(-160,100,14)
Vs1=np.linspace(-160,80,13)
Vs2=np.linspace(-160,60,12)
NO3=[140,70,35,17.5,0]
def line(x,a,b):
    return a*x+b

datadir="data/"


def Erev(Is):
    i1=-1
    if len(Is)==14:
        Vs=Vs0
    if len(Is)==13:
        Vs=Vs1
    if len(Is)==12:
        Vs=Vs2    
    for i in range(1,len(Is)+1):
        if Is[len(Is)-i]<0:
            i1=len(Is)-i
            break
    if i1<12:
        popt,pcov=curve_fit(line,Vs[i1-2:i1+2],Is[i1-2:i1+2])
    else:
        popt,pcov=curve_fit(line,Vs[10:14],Is[10:14])
    #print Is[i1-2:i1+2]
    return -popt[1]/popt[0]

def fna(NA,p1,p2):
    return ghk(0,0,.14,.115,.12,NA,p1,p2)
R=8.3144598e3
#Temperature in Kelvin
T=293.
F=96485.3329
def ghk(gluci,gluco,no3o,no3i,ki,ko,p1,p2):
    #p2=1e-19
    return R*T/F*np.log((p1*gluci+no3i+p2*ko)/(p1*gluco+no3o+p2*ki))


def f(NO3,p1,p2):
    
    return ghk(0,0.14-NO3,NO3,.115,.12,.14,p1,p2)

cells_tb_wt=[("05_06_20/05_06_20_z2.dat",(0,2,4,6,8,10,12,14,16,18)),
            ("05_06_20/05_06_20_z3.dat",(0,2,4,6,8,10,12,14,16,18)),
             ("05_06_20/05_06_20_z6.dat",(0,2,4,6,8,10,12,14,16,18)),
             ("08_06_20/08_06_20_z2.dat",(18,2,4,6,8,10,12,14,16,20)),
             ("08_06_20/08_06_20_z3.dat",(20,2,4,6,8,10,12,14,16,18)),
              ("08_06_20/08_06_20_z4.dat",(0,2,4,6,8,10,12,14,16,18)),
            ("09_06_20/09_06_20_z1.dat",(0,2,4,6,8,10,12,14,16,18)),
              ("09_06_20/09_06_20_z2.dat",(0,2,4,6,8,10,12,14,16,18)),
              ("09_06_20/09_06_20_z4.dat",(0,2,4,6,8,10,12,14,16,18)),
             ("09_06_20/09_06_20_z5.dat",(0,2,4,6,8,10,12,14,16,18)),
            ]

cells_tb_mut=[
             ("10_06_20/10_06_20_z1.dat",(0,2,4,6,8,10,12,14,16,18)),
            ("10_06_20/10_06_20_z3.dat",(0,2,4,6,8,10,12,14,16,18)),
    ("23_06_20/23_06_20_z2.dat",(0,2,4,6,8,10,12,14,16,18)),
    ("24_06_20/24_06_20_z1.dat",(0,2,4,6,8,10,12,14,16,18)),
     ("24_06_20/24_06_20_z2.dat",(0,2,4,6,8,10,12,14,16,18)),
     ("24_06_20/24_06_20_z3.dat",(0,2,4,6,8,10,12,14,16,18)),
    ("25_06_20/25_06_20_z2.dat",(0,2,4,6,8,10,12,14,16,18)),

    ("25_06_20/25_06_20_z5.dat",(0,2,4,6,8,10,12,14,16,18)),
    ("25_06_20/25_06_20_z6.dat",(0,2,4,6,8,10,12,14,16,18)),
    ("25_06_20/25_06_20_z7.dat",(0,2,4,6,8,10,12,14,16,18)),
    ("26_06_20/26_06_20_z1.dat",(0,2,4,6,8,10,12,14,16,18)),
     ("26_06_20/26_06_20_z2.dat",(0,2,4,6,8,10,12,14,16,18)),
     ("26_06_20/26_06_20_z3.dat",(0,2,4,6,8,10,12,14,16,18)),
     ("26_06_20/26_06_20_z4.dat",(0,2,4,6,8,10,12,14,16,18)),
     ("30_06_20/30_06_20_z1.dat",(0,2,4,6,8,10,12,14,16,18)),
     ("30_06_20/30_06_20_z2.dat",(0,2,4,6,8,10,12,14,16,18)),
     ("30_06_20/30_06_20_z3.dat",(0,2,4,6,8,10,12,14,16,18)),
     ("30_06_20/30_06_20_z4.dat",(0,2,4,6,8,10,12,14,16,18)),

            ]

cells_WTna=[("23_10_18/23_10_18_z1.dat",(2,4,6,8,10)),

            ("24_10_18/24_10_18_z4.dat",(2,4,6,8,10)),
            ("24_10_18/24_10_18_z5.dat",(2,4,6,8,10)),
            ("25_10_18/25_10_18_z1.dat",(4,6,8,10,12)),
            ("25_10_18/25_10_18_z4.dat",(2,4,7,9,11)),
            ("21_02_20/21_02_20_z1.dat",(1,3,5,7,9)),
             ("21_02_20/21_02_20_z2.dat",(1,3,5,7,9)),
            
             ("21_02_20/21_02_20_z4.dat",(1,3,5,7,9)),
             ("21_02_20/21_02_20_z5.dat",(1,3,5,7,9)),
             ("21_02_20/21_02_20_z6.dat",(1,3,5,7,9)),
         ]
cells_MUTna=[("23_10_18/23_10_18_z2.dat",(2,4,6,8,10)),
           ("24_10_18/24_10_18_z3.dat",(2,4,6,8,10)),

            ("25_10_18/25_10_18_z2.dat",(2,4,6,8,10)),
             ("25_10_18/25_10_18_z3.dat",(2,5,8,10,12)),
             ("20_02_20/20_02_20_z1.dat",(1,3,5,7,9)),
             ("20_02_20/20_02_20_z2.dat",(1,3,5,7,9)),
            
             ("20_02_20/20_02_20_z4.dat",(1,3,5,7,9)),
             ("20_02_20/20_02_20_z5.dat",(1,3,5,7,9)),
             ("20_02_20/20_02_20_z6.dat",(1,3,5,7,9)),
             ("20_02_20/20_02_20_z7.dat",(1,3,5,7,9)),
            ]

Erevs_MUT_tb=np.zeros(shape=(len(cells_tb_mut),5))
normIV_tb_MUT=np.zeros(shape=(len(cells_tb_mut),5,14))
k=0
for cell in cells_tb_mut:
    
    dat = gsfio.loadPatchmasterFile2(datadir+cell[0])
    colors=["k","r","g","b"]
    kk=0
    IVs=np.zeros(shape=(6,14))
    IVs_bg=np.zeros(shape=(6,14))

    for j in range(5):
        for i in range(14):
            IVs[kk,i]=np.mean(dat[cell[1][j]][i][5000:5100])
            IVs_bg[kk,i]=np.mean(dat[cell[1][j+5]][i][5000:5100])

        kk=kk+1
    ee=[]
    for i in range(5):
        
        normIV_tb_MUT[k,i,:]=IVs[i,:]-IVs_bg[i,:]
        Erevs_MUT_tb[k,i]=Erev(normIV_tb_MUT[k,i,:])
    

    k=k+1
Erevs_MUTna=np.zeros(shape=(len(cells_MUTna),5))
k=0
for cell in cells_MUTna:
    
    dat = gsfio.loadPatchmasterFile2(datadir+cell[0])
    colors=["k","r","g","b"]
    kk=0
    IVs=np.zeros(shape=(6,14))

    for j in cell[1]:
        for i in range(len(dat[j])):
            IVs[kk,i]=np.mean(dat[j][i][5000:5100])
        
        kk=kk+1
    ee=[]
    for i in range(5):    

        ee.append(Erev(IVs[i,:]))
        Erevs_MUTna[k,i]=Erev(IVs[i,:])

    k=k+1
Erevs_WT_tb=np.zeros(shape=(len(cells_tb_wt),5))
normIV_tb_wt=np.zeros(shape=(len(cells_tb_wt),5,14))
k=0
for cell in cells_tb_wt:
    
    dat = gsfio.loadPatchmasterFile2(datadir+cell[0])
    colors=["k","r","g","b"]
    kk=0
    IVs=np.zeros(shape=(6,14))
    IVs_bg=np.zeros(shape=(6,14))

    for j in range(5):
        for i in range(14):
            IVs[kk,i]=np.mean(dat[cell[1][j]][i][5000:5100])
            IVs_bg[kk,i]=np.mean(dat[cell[1][j+5]][i][5000:5100])

        kk=kk+1
    ee=[]
    for i in range(5):
        
        normIV_tb_wt[k,i,:]=IVs[i,:]-IVs_bg[i,:]
        Erevs_WT_tb[k,i]=Erev(normIV_tb_wt[k,i,:])
    

    k=k+1
    

Erevs_WTna=np.zeros(shape=(len(cells_WTna),5))
k=0
for cell in cells_WTna:
    
    dat = gsfio.loadPatchmasterFile2(datadir+cell[0])
    colors=["k","r","g","b"]
    kk=0
    IVs=np.zeros(shape=(6,13))

    for j in cell[1]:
        for i in range(len(dat[j])):
            IVs[kk,i]=np.mean(dat[j][i][5000:5100])
        
        kk=kk+1
    ee=[]
    for i in range(5):    

        ee.append(Erev(IVs[i,:]))
        Erevs_WTna[k,i]=Erev(IVs[i,:])

    k=k+1
xfit=[]
yfit=[]

    
xfit=xfit+[.142,.072,.037,.0185,0.01]
yfit=np.mean(Erevs_MUTna,axis=0)

poptMUTna,pcov=curve_fit(fna,np.array(xfit),yfit,bounds=[(0,0),(1,1)])
print poptMUTna,pcov


print "---------------------"
xfit=[]
yfit=[]
xfit=xfit+[.142,.072,.037,.0185,0.01]
yfit=np.mean(Erevs_WTna,axis=0)
poptWTna,pcov=curve_fit(fna,np.array(xfit),yfit,bounds=[(0,0),(100.,100.)])
print poptWTna,pcov

xfit=[]
yfit=[]
xfit=xfit+[.140,.070,.035,.017,0.]
yfit=np.mean(Erevs_MUT_tb,axis=0)
poptMUT,pcov=curve_fit(f,np.array(xfit),yfit,bounds=[(0.,0),(.5,poptMUTna[1])])
print poptMUT,pcov

print "---------------------"
xfit=[]
yfit=[]
xfit=xfit+[.140,.070,.035,.017,0.]
yfit=np.mean(Erevs_WT_tb,axis=0)
poptWT,pcov=curve_fit(f,np.array(xfit),yfit,bounds=[(0,0),(.10,poptWTna[1])])
print poptWT,pcov


plt.figure(figsize=(3,3))

plt.errorbar(NO3,np.mean(Erevs_WT_tb,axis=0),yerr=np.std(Erevs_WT_tb,axis=0),fmt="o",color="k")
plt.plot(np.linspace(150,0.,100),f(np.linspace(.150,0.,100),*poptWT),color="k",label="WT EAAT2")
plt.errorbar(NO3,np.mean(Erevs_MUT_tb,axis=0),yerr=np.std(Erevs_MUT_tb,axis=0),fmt="o",color="r")
plt.plot(np.linspace(150,0.,100),f(np.linspace(.150,0.,100),*poptMUT),color="r",label="L46P EAAT2")
plt.xlim(-10,150)
plt.ylim(-15,90)
plt.xlabel("[NO3] (mM)")
plt.ylabel("Erev (mV)")
plt.savefig("NO3.svg")
plt.show()

plt.figure(figsize=(3,3))
plt.errorbar([142,72,37,18.5,10],np.mean(Erevs_MUTna,axis=0),yerr=np.std(Erevs_MUTna,axis=0),fmt="o",color="r")
plt.plot([142,72,37,18.5,10],fna(np.array([.142,.072,.037,.0185,0.01]),*poptMUTna),color="r", label="L46P EAAT2")

plt.errorbar([142,72,37,18.5,10],np.mean(Erevs_WTna,axis=0),yerr=np.std(Erevs_WTna,axis=0),fmt="o",color="k")
plt.plot([142,72,37,18.5,10],fna(np.array([.142,.072,.037,.0185,0.01]),*poptWTna),color="k",label="WT EAAT2")
plt.xlim(-10,150)
plt.ylim(-15,90)
plt.xlabel("[Na] (mM)")
plt.ylabel("Erev (mV)")
plt.savefig("Na.svg")
plt.show()




plt.figure(figsize=(3,3))
for i in range(5):
    plt.errorbar([-80,-60,-40,-20,0,20,40,60,80],np.mean(normIV_tb_wt,axis=0)[i][:9],yerr=np.std(normIV,axis=0)[i][:9],fmt="o-",label=str(NO3[i]))
plt.plot([-80,80],[0,0],color="k")
plt.plot([0,0],[-1.5,1.0],color="k")
plt.legend(loc="best")
plt.show()

plt.figure(figsize=(3,3))
for i in range(5):
    plt.errorbar([-80,-60,-40,-20,0,20,40,60,80],np.mean(normIV_tb_mut,axis=0)[i][:9],yerr=np.std(normIV_MUT,axis=0)[i][:9],fmt="o-",label=str(NO3[i]))
plt.plot([-80,80],[0,0],color="k")
plt.plot([0,0],[-1.5,1.0],color="k")
plt.legend(loc="best")
plt.show()


