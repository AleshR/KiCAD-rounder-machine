#!/usr/bin/python3.6
import numpy as np
import matplotlib.pyplot as plt

print("Hi, this is generator for ring placement:")

def vstup():
    print("Please input parameters")
    centerX = float(input('Enter center of circle X-axis: '))
    centerY = float(input('Enter center of circle Y-axis: '))
    nt = int(input('Enter number of parts: '))
    dia = float(input('Enter diameter of circle: '))
    

    plot(dia, nt, centerX, centerY)

def plot(diam, count, cX, cY):

    real = np.zeros((count),dtype=float)
    imag = np.zeros((count),dtype=float)
    
    angle = (2*np.pi)/count

    for i in range(count):
        real[i] = (diam/2)*(np.cos(angle*i))+cX
        imag[i] = (diam/2)*(np.sin(angle*i))+cY

    real = np.around(real, decimals=2)
    imag = np.around(imag, decimals=2)
    
    
            # print(real)
            # print(imag)

    
    diameter = (diam/2)+1

    plt.scatter(real,imag)
    plt.xlim(-diameter+cX, diameter+cX)
    plt.ylim(-diameter+cY,diameter+cY)

    for i in range(count):
        print("Element: ",i)
        print("X: ", real[i])
            #plt.annotate(real[i],(real[i],imag[i]-1))
        print("Y: ", imag[i])
            #plt.annotate(imag[i],(real[i],imag[i]-1.7))
        print("-------------------------------------")
    
    plt.ylabel('Y position')
    plt.xlabel('X position')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

vstup()
