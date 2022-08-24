import numpy  as np
import matplotlib.pyplot as plt
plt.figure(figsize=(7,10))
plt.rc('font', family='arial', size=12)
plt.rc('axes', linewidth=2)

data1 = np.loadtxt('profile-evp20-train.ascii')
data2 = np.loadtxt('profile-evp20-test.ascii')
data3 = np.loadtxt('profile-evp21-test.ascii')

cnt1 = data1[:, 13]
cnt2 = data2[:, 13]
cnt3 = data3[:, 13]

y   = data1[:, 0]/1000

plt.subplot(1,1,1)
plt.xlim(0, 600000)
plt.ylim(00, 15)
plt.plot(cnt1, y, color='red',  linewidth=2, linestyle='solid',  label='Train20')
plt.plot(cnt2, y, color='blue',   linewidth=2, linestyle='solid',  label='Test20')
plt.plot(cnt3, y, color='green',  linewidth=2, linestyle='solid', label='Test21')
plt.ylabel('Height(Km)',fontsize=15)
plt.xlabel('Count',fontsize=15)
plt.yticks(np.arange(00,  16, 1))
plt.xticks(np.arange(0, 700000, 100000))
plt.axvline(x=0, ymin=0, ymax=15, color='black')
plt.legend(loc='upper center', frameon=False, ncol=2)
plt.title("Number of Points", fontsize=14, color='black')

#plt.grid()
plt.savefig('count-profile.png', format='png', dpi=600)
plt.show()
