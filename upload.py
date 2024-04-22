

import httpx
import json
import numpy as np
import matplotlib.pyplot as plt
import matlab.engine
import scipy.io
import json
import os
from supabase import create_client, Client
import math
import random
from processes import *



def simulate(input):
    eng = matlab.engine.start_matlab()
    faulty, noFaulty = eng.simulate(nargout=2)
    
    if input:
        return np.asarray(faulty[0])
    else:
        return np.asarray(noFaulty[0])
    


def uploadTestData(faulty):
    accelerometer_data = []
    n = 0

    # Simulate x-axis data
    x_data = simulate(faulty).tolist()[0]
    print(len(x_data))

    # Simulate y-axis data
    y_data = simulate(faulty).tolist()[0]

    for i in range(len(x_data)):
        # Calculate time for the current reading

        # Calculate the rotation angle for the current time

        # Calculate acceleration values based on the rotation angle
        x = x_data[i]
        y = y_data[i]
        z = random.uniform(0.0, 2.0)

        # Create a reading dictionary
        reading = {
            'pos': n,
            'x': x,
            'y': y,
            'z': z
        }

        # Append the reading to the data list
        accelerometer_data.append(reading)
        n += 1

    # Convert accelerometer data to JSON format
    json_data = json.dumps(accelerometer_data)


    # Upload data to Supabase
    url = "https://ljzrkwoyewivcfhthral.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqenJrd295ZXdpdmNmaHRocmFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDA1NzU3NzcsImV4cCI6MjAxNjE1MTc3N30.bSMt5zZF012w-YVjnLTKJO0yAeMonr7VgserYfadoPM"
    supabase = create_client(url, key)

    data, count = supabase.table('Raw').insert({
        "measurement": json_data,
        "average_temperature": str(random.randint(25, 42)),
        "sampling_frequency": "1000"
    }).execute()

    return data, count

   
def upload_fft_data(x_values, y_values, z_values):
    
    # Create a dictionary to store the FFT result
    fft_json = {
        'x': x_values,
        'y': y_values,
        'z': z_values
    }

    json_string = json.dumps(fft_json)

    url = "https://ljzrkwoyewivcfhthral.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqenJrd295ZXdpdmNmaHRocmFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDA1NzU3NzcsImV4cCI6MjAxNjE1MTc3N30.bSMt5zZF012w-YVjnLTKJO0yAeMonr7VgserYfadoPM"
    supabase = create_client(url, key)

    data, count = supabase.table('FFT').insert({"measurement": json_string}).execute()

    if count == 1:
        print("FFT data uploaded successfully.")
    else:
        print("Error uploading FFT data.")

def uploadFaulty(faulty,id):
    url = "https://ljzrkwoyewivcfhthral.supabase.co"
    key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqenJrd295ZXdpdmNmaHRocmFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDA1NzU3NzcsImV4cCI6MjAxNjE1MTc3N30.bSMt5zZF012w-YVjnLTKJO0yAeMonr7VgserYfadoPM"
    supabase = create_client(url, key)
    data, count = supabase.table('detection').insert({'id':id, "faulty": faulty}).execute()

def upload_tsa_data(x_values, y_values, z_values):
    # Create an instance of the Processes class

    # Run the TSA process for each axis
    tsa_result_x = TSA(x_values, 1000.0, 13.0, 35.0, 22.5)
    tsa_result_y = TSA(y_values, 1000.0, 13.0, 35.0, 22.5)
    tsa_result_z = TSA(z_values, 1000.0, 13.0, 35.0, 22.5)
    

    # Convert the TSA results to JSON
    tsa_json = {
        'x': JSONconvert(tsa_result_x),
        'y': JSONconvert(tsa_result_y),
        'z': JSONconvert(tsa_result_z)
    }

    json_string = json.dumps(tsa_json)
    

    url = "https://ljzrkwoyewivcfhthral.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqenJrd295ZXdpdmNmaHRocmFsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDA1NzU3NzcsImV4cCI6MjAxNjE1MTc3N30.bSMt5zZF012w-YVjnLTKJO0yAeMonr7VgserYfadoPM"
    supabase = create_client(url, key)

    data, count = supabase.table('TSA').insert({"measurement": json_string}).execute()

    if count == 1:
        print("TSA data uploaded successfully.")
    else:
        print("Error uploading TSA data.")
    return tsa_result_x, tsa_result_y, tsa_result_z

# Example usage:

