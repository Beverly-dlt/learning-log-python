# NAME : Beverly Machawi
#
#ID: 90036891
#
# plotNumber.py - MNIST Dataset [1] plotting with matplotlib
#

import matplotlib.pyplot as plt
import numpy as np


def readdata(filename):
    data = []
    file1 = open(filename,'r')
    lines = file1.readlines()
    print(lines)
    for line in lines:
        splitline =  line.strip().split(',')
    data.append([int(x) for x in splitline])
    file1.close()
    return data

def convertArray(data):
    dataarray = np.array(data)
    return dataarray

def rowToImage(dataarray):
    data3D = []
    for d in dataarray:
        data3D.append(dataarray.reshape(28,28))
    return data3D

def plotImages(data3D):
     plt.figure(1)
     plt.subplot(241)
     plt.imshow(data3D[0], cmap = plt.cm.gray)
     plt.savefig('finalplot.png')


     plt.show()
     

def main():
    filename = input("Enter filename with extension ... ")
    print('\nData read from file - represeting 1st image :')
    data = readdata(filename)
    print(data[0])
    dataarray = convertArray(data)
    print('\nData converted to array - representing 1st image only\n')
    print(dataarray[0])
    data3D = rowToImage(dataarray)
    print('\nData converted to 3D list - representing 1st image only\n')
    print(data3D[0])
    print('\nPlotting images\n')
    plotImages(data3D)
    print("End of code")
if __name__ == '__main__':
        main()


