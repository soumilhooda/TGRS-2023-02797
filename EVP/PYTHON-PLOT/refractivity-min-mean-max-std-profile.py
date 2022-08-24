import numpy  as np
import matplotlib.pyplot as plt
plt.figure(figsize=(7,10))
plt.rc('font', family='arial', size=12)
plt.rc('axes', linewidth=2)

data1 = np.loadtxt('evp-corr-ucar-india.ascii')

min = data1[:, 6]
mean = data1[:, 7]
max = data1[:, 8]
std = data1[:, 9]

y   = data1[:, 0]/1000

plt.subplot(1,1,1)
plt.xlim(0, 400)
plt.ylim(00, 15)
plt.plot(min, y, color='red',  linewidth=2, linestyle='solid',  label='Minimum')
plt.plot(mean, y, color='blue',   linewidth=2, linestyle='solid',  label='Mean')
plt.plot(max, y, color='green',  linewidth=2, linestyle='solid', label='Maximum')
plt.plot(std, y, color='cyan',  linewidth=2, linestyle='solid', label='Std.Dev')
plt.ylabel('Height(Km)',fontsize=15)
plt.xlabel('Refractivity',fontsize=15)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(0, 425, 25))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='upper center', frameon=False, ncol=1)
plt.title("Refractivity", fontsize=14, color='black')

#plt.grid()
plt.savefig('refractivity-min-mean-max-std-profile.png', format='png', dpi=600)
plt.show()
