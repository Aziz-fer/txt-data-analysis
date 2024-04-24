
"""
-*- Operating on different coding systems: utf-8 -*-
Created on Sat Oct 27 16:57:23 2024
@author: AzizFer
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

def number_conversion(number, system):
    if number < 0:
        symbol = -1
    else:
        symbol = 1
    number = symbol*number
    converted_number = 0
    for i in range(len(str(number))):
        converted_number += number % 10 * system**i
        number = number//10
    return converted_number*symbol

data = []
Temperatures = []
Times = []
files = [["data\data_binary.txt", 2], ["data\data_quad.txt", 4], ["data\data_octal.txt", 8]]

def load_data(file_name, system):
    source_file = open(file_name, 'r')
    
    while True:
        current_line = source_file.readline()
        if current_line == '':
            break
        data.append(current_line)
    source_file.close()
        
    for i in range(len(data)):
        actual_record = data[i].split(" ")
        Times.append(actual_record[0])
        Temperatures.append(actual_record[1])
        
        Times[i] = number_conversion(int(Times[i]), system)
        Temperatures[i] = number_conversion(int(Temperatures[i]), system)

def defaultExecute():
    for file in files:
        print(file[1])
        load_data(file[0], file[1])
        plt.figure(dpi=250)
        plt.plot(Times, Temperatures, color='orange')  # Set the plot color to orange
        plt.title(file[0][5:-4])  # since the file name starts with 'data\', so we skip the first 5 characters
        plt.xlabel('Time in Hours')  # Set the x-axis label to 'Time'
        plt.ylabel('Temperature')  # Set the y-axis label to 'Temperature'
        plt.tight_layout()
        plt.savefig(file[0][:-4] + ".png")
        plt.close()  # Ensure to close the plot to avoid memory issues
        data.clear()
        Times.clear()
        Temperatures.clear()

def executeWithOptions(grid: bool, dpi2: int, dotcolor: str):
    for file in files:
        print(file[1])
        load_data(file[0], file[1])
        Times_np = np.array(Times, dtype=float)  # Ensure Times is a NumPy array of floats
        Temperatures_np = np.array(Temperatures, dtype=float)  # Ensure Temperatures is a NumPy array of floats
        
        # Create a spline of your data
        X_Y_Spline = make_interp_spline(Times_np, Temperatures_np)
        X_ = np.linspace(min(Times_np), max(Times_np), 500)  # 500 represents the number of interpolation points
        Y_ = X_Y_Spline(X_)

        plt.figure(dpi=dpi2)
        plt.plot(X_, Y_, color=dotcolor)  # Plot the smoothed curve
        plt.title(file[0][5:-4])
        plt.xlabel('Time in Hours')
        plt.ylabel('Temperature')
        plt.grid(grid)
        plt.tight_layout()
        plt.legend(['Temperature'])
        plt.annotate('Max Temp', xy=(Times[np.argmax(Temperatures)], max(Temperatures)), 
             xytext=(Times[np.argmax(Temperatures)], max(Temperatures) + 5),
             arrowprops=dict(facecolor='black', shrink=0.05))

        plt.savefig(file[0][:-4] + ".png")
        plt.close()

        data.clear()
        Times.clear()
        Temperatures.clear()

def plot_section_of_time(file_name, system, time_interval):
    load_data(file_name, system)
    Times_np = np.array(Times, dtype=float)  # Ensure Times is a NumPy array of floats
    Temperatures_np = np.array(Temperatures, dtype=float)  # Ensure Temperatures is a NumPy array of floats

    # Create a spline of your data
    X_Y_Spline = make_interp_spline(Times_np, Temperatures_np)
    X_ = np.linspace(min(Times_np), max(Times_np), 500)
    Y_ = X_Y_Spline(X_)

    plt.figure(dpi=250)
    plt.plot(X_, Y_, color="green")
    plt.title(file_name[5:-4])  # Adjust the slicing according to your file naming conventions
    plt.xlabel('Time in Hours')
    plt.ylabel('Temperature')
    plt.xlim(time_interval)  # Set the limits for the x-axis
    plt.tight_layout()
    plt.legend(['Temperature'])
    plt.annotate('Max Temp', xy=(Times[np.argmax(Temperatures)], max(Temperatures)), 
         xytext=(Times[np.argmax(Temperatures)], max(Temperatures) + 5),
         arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()
    plt.close()

    data.clear()
    Times.clear()
    Temperatures.clear()


# Example of calls usages:
plot_section_of_time("data/data_octal.txt", 8, [0, 1000])
#executeWithOptions(True,250,'red')
#defaultExecute()
