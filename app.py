from flask import Flask
import schedule
import time
import threading
from upload import *
from recieve import retrieveAndConvertData
from processes import *
from upload import upload_fft_data
from detect import isGearFaulty
import httpx


app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask Server'

def fftComb(x,y,z,tx,ty,tz):
    print("fft")
    xfft = fft(x, 1000)
    yfft = fft(y, 1000)
    zfft = fft(z, 1000)
    print("faulty")
    faulty = isGearFaulty(x, y, z, xfft, yfft, zfft,tx,ty,tz)
    upload_fft_data(xfft, yfft, zfft)
    print(faulty)
    uploadFaulty(faulty,1)
    


def upload_data():
    retry_limit = 3  # Maximum number of retry attempts
    retry_count = 0  # Current retry attempt count

    while retry_count < retry_limit:
        try:
            # Call the uploadTestData() function here
            uploadTestData(True)
            x, y, z, id = retrieveAndConvertData()
            print('Retrieved')
            tx,ty,tz = upload_tsa_data(x, y, z)
            fftComb(x, y, z,tx,ty,tz)
            print("rest")

            break  # Break the loop if the code runs successfully
        except httpx.WriteTimeout:
            retry_count += 1
            print(f"Retry attempt {retry_count} of {retry_limit} due to httpx.WriteTimeout")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            break  # Break the loop if an unexpected error occurs

    if retry_count == retry_limit:
        print(f"Maximum retry attempts reached. Failed to execute the function.")

    

    
schedule.every(10).seconds.do(upload_data)

# Create a separate thread to run the scheduled tasks
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    # Start the scheduler thread
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()

    # Run the Flask server
    app.run()