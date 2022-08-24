import numpy  as np
import matplotlib.pyplot as plt
plt.figure(figsize=(12,7))
plt.rc('font', family='arial', size=12)
plt.rc('axes', linewidth=2)

data1 = np.loadtxt('profile-tmp20-train.ascii')
data2 = np.loadtxt('profile-tmp20-test.ascii')
data3 = np.loadtxt('profile-tmp21-test.ascii')

ostd1 = data1[:, 4]
bias1 = data1[:, 9]
rms1 = data1[:, 10]
std1 = data1[:, 11]

ostd2 = data2[:, 4]
bias2 = data2[:, 9]
rms2 = data2[:, 10]
std2 = data2[:, 11]

ostd3 = data3[:, 4]
bias3 = data3[:, 9]
rms3 = data3[:, 10]
std3 = data3[:, 11]

y   = data1[:, 0]/1000

plt.subplot(1,3,1)
plt.xlim(-0.9, 0.3)
plt.ylim(00, 15)
plt.plot(bias1, y, color='red',  linewidth=2, linestyle='solid',  label='Train20')
plt.plot(bias2, y, color='blue',   linewidth=2, linestyle='solid',  label='Test20')
plt.plot(bias3, y, color='green',  linewidth=2, linestyle='solid', label='Test21')
plt.ylabel('Height(Km)',fontsize=15)
plt.xlabel('Bias(K)',fontsize=15)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(-0.9, 0.6, 0.3))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(a) Mean Difference", fontsize=14, color='black')

plt.subplot(1,3,2)
plt.xlim(0, 2.1)
plt.ylim(00, 15)
plt.plot(rms1, y, color='red',  linewidth=2, linestyle='solid',  label='Train20')
plt.plot(rms2, y, color='blue',   linewidth=2, linestyle='solid',  label='Test20')
plt.plot(rms3, y, color='green',  linewidth=2, linestyle='solid', label='Test21')
#plt.ylabel('Height(Km)',fontsize=15)
plt.xlabel('RMSE(K)',fontsize=15)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(00, 2.4, 0.3))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(b) Root Mean Square Error", fontsize=14, color='black')

plt.subplot(1,3,3)
plt.xlim(0, 2.1)
plt.ylim(00, 15)
plt.plot(std1, y, color='red',  linewidth=2, linestyle='solid',  label='Train20')
plt.plot(std2, y, color='blue',   linewidth=2, linestyle='solid',  label='Test20')
plt.plot(std3, y, color='green',  linewidth=2, linestyle='solid', label='Test21')
#plt.ylabel('Height(Km)',fontsize=15)
plt.xlabel('Std.Dev(K)',fontsize=15)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(00, 2.4, 0.3))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='best', frameon=False, ncol=1)
plt.title("(c) Standard Deviation", fontsize=14, color='black')

#plt.grid()
plt.savefig('tmp-bias-rmsd-std-profile.png', format='png', dpi=600)
plt.show()
