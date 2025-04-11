#Author: Beverly Machawi
#ID: 90036891
#
# PractTest02: Assessment submission implementation
import numpy as np
import matplotlib.pyplot as plt

xvalues = np.arange(0,360,10)
print(' Xvalues:',xvalues)

#sin theta

SinTheta = np.sin(xvalues)
print('SinTheta: ',SinTheta)

log = np.log(xvalues)
print('Log: ', log)

sum_sin_log = SinTheta + log
# plotting

plt.subplot(131)
plt.title('plotting sum')
plt.plot(xvalues, sum_sin_log 'r+')
plt.xlabel('sum of log and log')
plt.ylabel('xvalues')

plt.subplot(132)
plt.title('plotting log')
plt.plot(xvalues, log 'g-.')
plt.xlabel('log')
plt.ylabel('xvalues'
        )
plt.subplot(133)
plt.title('plotting Sin Theta')
plt.plot(xvalues, SinTheta 'g-')
plt.xlabel('Sin Theta')
plt.ylabel('xvalues')

plt.show()


