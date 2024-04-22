import numpy as np
import matlab.engine
from recieve import retrieveAndConvertData
import matplotlib.pyplot as plt
import math
import random


  
def fft(values, readingFreq):
    N = len(values)
    # Sample spacing
    T = 1.0 / readingFreq

    # Perform FFT
    yf = np.fft.fft(values)
    xf = np.fft.fftfreq(N, T)[:N//2]

    print(values)

    # Create a dictionary of frequency and corresponding values
    result = {}
    for i in range(len(xf)):
        result[xf[i]] = 2.0 / N * np.abs(yf[i])

    return result

def simulate(input):
    eng = matlab.engine.start_matlab()
    faulty, noFaulty = eng.simulate(nargout=2)
    if input:
        return np.asarray(faulty[0])
    else:
        return np.asarray(noFaulty[0])
    

# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0 
x = np.linspace(0.0, N*T, N, endpoint=False)

y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)


def flatten_matrix(matrix):
    flattened_list = [item for sublist in matrix for item in sublist]
    return flattened_list


def TSA(values, readingFreq, Pteeths, Gteeths, shaftFreq):
    eng = matlab.engine.start_matlab()

    # Prepare the input array for MATLAB
    input_array = values

    # Call the MATLAB function
    pinTSA, gearTSA, pinAmp, gearAmp = eng.getTsa(
        readingFreq, Pteeths, Gteeths, shaftFreq, input_array, nargout=4
    )

    # Convert MATLAB matrices to NumPy arrays
    pinTSA = np.array(pinTSA)
    gearTSA = np.array(gearTSA)
    pinAmp = np.array(pinAmp)
    gearAmp = np.array(gearAmp)

    # Flatten the matrices
    pinTSA = flatten_matrix(pinTSA)
    gearTSA = flatten_matrix(gearTSA)
    pinAmp = flatten_matrix(pinAmp)
    gearAmp = flatten_matrix(gearAmp)
    pinArray = {}
    for i in range(len(pinTSA)):
        pinArray[pinAmp[i]] = pinTSA[i]

  


    gearArray = {}
    for i in range(len(gearTSA)):
        pinArray[gearAmp[i]] = gearTSA[i]

    return pinArray, gearArray

def convert_values_to_float(dictionary):
    for key in dictionary:
        dictionary[key] = float(dictionary[key])
    return dictionary

def JSONconvert(array):
    json_data = {}
    i = 0
    print("sdfd")
   
    print(array[0].items())
    print("")
    for key, value in array[0].items():
        json_data[i] = {"KEY": key, "VALUE": float(value)}
        i += 1
    print("start", json_data)

    return json_data



