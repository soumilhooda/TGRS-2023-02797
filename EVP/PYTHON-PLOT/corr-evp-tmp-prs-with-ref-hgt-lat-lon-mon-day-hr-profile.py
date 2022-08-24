import numpy  as np
import matplotlib.pyplot as plt
plt.figure(figsize=(16,12))
plt.rc('font', family='arial', size=12)
plt.rc('axes', linewidth=2)

data1 = np.loadtxt('evp-corr-ucar-india.ascii')
data2 = np.loadtxt('tmp-corr-ucar-india.ascii')
data3 = np.loadtxt('prs-corr-ucar-india.ascii')

eref = data1[:, 10]
ehgt = data1[:, 11]
elat = data1[:, 12]
elon = data1[:, 13]
emon = data1[:, 14]
eday = data1[:, 15]
ehrs = data1[:, 16]

tref = data2[:, 10]
thgt = data2[:, 11]
tlat = data2[:, 12]
tlon = data2[:, 13]
tmon = data2[:, 14]
tday = data2[:, 15]
thrs = data2[:, 16]

pref = data3[:, 10]
phgt = data3[:, 11]
plat = data3[:, 12]
plon = data3[:, 13]
pmon = data3[:, 14]
pday = data3[:, 15]
phrs = data3[:, 16]

y   = data1[:, 0]/1000

plt.subplot(2,4,1)
plt.xlim(0, 1)
plt.ylim(00, 15)
plt.plot(eref, y, color='red',  linewidth=2, linestyle='solid',  label='e')
plt.plot(tref, y, color='blue',   linewidth=2, linestyle='solid',  label='T')
plt.plot(pref, y, color='green',  linewidth=2, linestyle='solid', label='P')
plt.ylabel('Height(Km)',fontsize=13)
plt.xlabel('Correlation',fontsize=13)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(0, 1.2, 0.2))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(a) Correlation with Refractivity ", fontsize=12, color='black')

plt.subplot(2,4,2)
plt.xlim(-1, 0)
plt.ylim(00, 15)
plt.plot(ehgt, y, color='red',  linewidth=2, linestyle='solid',  label='e')
plt.plot(thgt, y, color='blue',   linewidth=2, linestyle='solid',  label='T')
plt.plot(phgt, y, color='green',  linewidth=2, linestyle='solid', label='P')
plt.xlabel('Correlation',fontsize=13)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(-1, 0.2, 0.2))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(b) Correlation with Height ", fontsize=12, color='black')

plt.subplot(2,4,3)
plt.xlim(-0.8, 0.8)
plt.ylim(00, 15)
plt.plot(elat, y, color='red',  linewidth=2, linestyle='solid',  label='e')
plt.plot(tlat, y, color='blue',   linewidth=2, linestyle='solid',  label='T')
plt.plot(plat, y, color='green',  linewidth=2, linestyle='solid', label='P')
plt.xlabel('Correlation',fontsize=13)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(-0.8, 1.0, 0.2))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(c) Correlation with Latitude ", fontsize=12, color='black')

plt.subplot(2,4,4)
plt.xlim(-0.6, 0.6)
plt.ylim(00, 15)
plt.plot(elon, y, color='red',  linewidth=2, linestyle='solid',  label='e')
plt.plot(tlon, y, color='blue',   linewidth=2, linestyle='solid',  label='T')
plt.plot(plon, y, color='green',  linewidth=2, linestyle='solid', label='P')
plt.xlabel('Correlation',fontsize=13)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(-0.6, 0.8, 0.2))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(d) Correlation with Longitude ", fontsize=12, color='black')

plt.subplot(2,4,5)
plt.xlim(-0.3, 0.3)
plt.ylim(00, 15)
plt.plot(emon, y, color='red',  linewidth=2, linestyle='solid',  label='e')
plt.plot(tmon, y, color='blue',   linewidth=2, linestyle='solid',  label='T')
plt.plot(pmon, y, color='green',  linewidth=2, linestyle='solid', label='P')
plt.ylabel('Height(Km)',fontsize=13)
plt.xlabel('Correlation',fontsize=13)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(-0.3, 0.4, 0.1))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(e) Correlation with Month ", fontsize=12, color='black')

plt.subplot(2,4,6)
plt.xlim(-0.3, 0.3)
plt.ylim(00, 15)
plt.plot(eday, y, color='red',  linewidth=2, linestyle='solid',  label='e')
plt.plot(tday, y, color='blue',   linewidth=2, linestyle='solid',  label='T')
plt.plot(pday, y, color='green',  linewidth=2, linestyle='solid', label='P')
plt.xlabel('Correlation',fontsize=13)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(-0.3, 0.4, 0.1))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(f) Correlation with Day ", fontsize=12, color='black')

plt.subplot(2,4,7)
plt.xlim(-0.3, 0.3)
plt.ylim(00, 15)
plt.plot(ehrs, y, color='red',  linewidth=2, linestyle='solid',  label='e')
plt.plot(thrs, y, color='blue',   linewidth=2, linestyle='solid',  label='T')
plt.plot(phrs, y, color='green',  linewidth=2, linestyle='solid', label='P')
plt.xlabel('Correlation',fontsize=13)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(-0.3, 0.4, 0.1))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(g) Correlation with Hour ", fontsize=12, color='black')

#plt.grid()
plt.savefig('corr-evp-tmp-prs-with-ref-hgt-lat-lon-mon-day-hr-profile.png', format='png', dpi=600)
plt.show()
