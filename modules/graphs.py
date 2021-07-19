import numpy as np
import matplotlib.pyplot as plt

"""
figure template

plt.figure(_int_)
plt.plot(_array_,_array_, label=_string_, color=_string_)
plt.xlabel(_string_)
plt.ylabel(_string_)
plt.title(_string_)
plt.legend()
plt.grid()
plt.grid(which="minor", alpha=0.25))
plt.minorticks_on()
plt.show()
"""

def setGrid(xLabel=None, yLabel=None, title=None):
    """Configures axis labels, title and other roperties"""
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.grid(which="minor", alpha=0.25)
    plt.minorticks_on()

def plotBestFit(x,y, matchY=False, degree=1, plotLabel=None, plotColour="tab:blue"):
    """Plots the best fit curve of given degree to fit given numpy arrays"""
    m,c = np.polyfit(x,y,degree)
    plt.plot(x,y,"o", color=plotColour)
    
    if (matchY):
        extrapolatedX=(np.array([y[0],y[-1]])-c)/m
        plt.plot(extrapolatedX,m*extrapolatedX+c, label=plotLabel, color=plotColour)
    
    else:
        plt.plot(x,m*x+c, label=plotLabel, color=plotColour)