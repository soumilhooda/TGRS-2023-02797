import numpy  as np
import matplotlib.pyplot as plt
plt.figure(figsize=(13,7))
plt.rc('font', family='arial', size=12)
plt.rc('axes', linewidth=2)

data1 = np.loadtxt('profile-prs20-train.ascii')
data2 = np.loadtxt('profile-prs20-test.ascii')
data3 = np.loadtxt('profile-prs21-test.ascii')

min1 = data1[:, 1]
mean1 = data1[:, 2]
max1 = data1[:, 3]
std1 = data1[:, 4]

min2 = data2[:, 1]
mean2 = data2[:, 2]
max2 = data2[:, 3]
std2 = data2[:, 4]

min3 = data3[:, 1]
mean3 = data3[:, 2]
max3 = data3[:, 3]
std3 = data3[:, 4]

y   = data1[:, 0]/1000

plt.subplot(1,3,1)
plt.xlim(100, 1050)
plt.ylim(00, 15)
plt.plot(min1, y, color='red',  linewidth=2, linestyle='solid',  label='Minimum')
plt.plot(mean1, y, color='blue',   linewidth=2, linestyle='solid',  label='Mean')
plt.plot(max1, y, color='green',  linewidth=2, linestyle='solid', label='Maximum')
plt.plot(std1, y, color='cyan',  linewidth=2, linestyle='solid', label='Std.Dev')
plt.ylabel('Height(Km)',fontsize=15)
plt.xlabel('P(hPa)',fontsize=15)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(100, 1200, 200))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(a) Train20", fontsize=14, color='black')

ax2 = plt.twiny()  # instantiate a second axes that shares the same x-axis
plt.xlim(0, 20)
plt.xticks(np.arange(0, 22, 2))
#ax2.set_xlabel( color='cyan',size=20)  # we already handled the x-label with ax1
ax2.plot(std1, y, color='cyan',  linewidth=2, linestyle='solid', label='Std.Dev')
ax2.tick_params(axis='x', labelcolor='cyan',width=2,size=5)
#ax2.legend(loc='center', frameon=False, ncol=1)
#fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.subplot(1,3,2)
plt.xlim(100, 1050)
plt.ylim(00, 15)
plt.plot(min2, y, color='red',  linewidth=2, linestyle='solid',  label='Minimum')
plt.plot(mean2, y, color='blue',   linewidth=2, linestyle='solid',  label='Mean')
plt.plot(max2, y, color='green',  linewidth=2, linestyle='solid', label='Maximum')
plt.plot(std2, y, color='cyan',  linewidth=2, linestyle='solid', label='Std.Dev')
#plt.ylabel('Height(Km)',fontsize=15)
plt.xlabel('P(hPa)',fontsize=15)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(100, 1200, 200))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(b) Test20", fontsize=14, color='black')

ax2 = plt.twiny()  # instantiate a second axes that shares the same x-axis
plt.xlim(0, 20)
plt.xticks(np.arange(0, 22, 2))
ax2.plot(std2, y, color='cyan',  linewidth=2, linestyle='solid', label='Std.Dev')
ax2.tick_params(axis='x', labelcolor='cyan',width=2,size=5)

plt.subplot(1,3,3)
plt.xlim(100, 1050)
plt.ylim(00, 15)
plt.plot(min3, y, color='red',  linewidth=2, linestyle='solid',  label='Minimum')
plt.plot(mean3, y, color='blue',   linewidth=2, linestyle='solid',  label='Mean')
plt.plot(max3, y, color='green',  linewidth=2, linestyle='solid', label='Maximum')
plt.plot(std3, y, color='cyan',  linewidth=2, linestyle='solid', label='Std.Dev')
plt.xlabel('P(hPa)',fontsize=15)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(100, 1200, 200))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(c) Test21", fontsize=14, color='black')

ax2 = plt.twiny()  # instantiate a second axes that shares the same x-axis
plt.xlim(0, 20)
plt.xticks(np.arange(0, 22, 2))
ax2.plot(std3, y, color='cyan',  linewidth=2, linestyle='solid', label='Std.Dev')
ax2.tick_params(axis='x', labelcolor='cyan',width=2,size=5)

#plt.grid()
plt.savefig('prs-min-mean-max-std-stats-profile.png', format='png', dpi=600)
plt.show()
