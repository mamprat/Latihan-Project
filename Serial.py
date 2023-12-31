import serial
import requests
import time
import json
import traceback
from flask import Flask, jsonify

serial_port = 'COM4'
baud_rate = 9600

app = Flask(__name__)

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    data_collection_duration = config.get("data_collection_duration_seconds", 5)

def collect_data():
    data_list = []
    start_time = time.time() 
    while (time.time() - start_time) < data_collection_duration:
        line = ser.readline().decode().strip()
        data_list.append(line) 
        print(line) 
    return data_list

ser = serial.Serial(serial_port, baud_rate)

while True:
    try:
        collected_data = collect_data()
        api_endpoint = 'http://127.0.0.1:5000/' 
        payload = {'data': collected_data}

        response = requests.post(api_endpoint, json=payload)
        if response.status_code == 200:
            print("Data sent successfully!")
            break  
    
    except KeyboardInterrupt:
        print("Program stopped by the user.")
        break  # Exit the loop if stopped by the user

    except Exception as e:
        with open('error.log', 'a') as error_log:
            error_log.write(f"An error occurred: {str(e)}\n")
            error_log.write(f"Traceback: {traceback.format_exc()}\n")
        print("An error occurred. Retrying in 1 minute...")
        time.sleep(60)  # Wait for 5 seconds before retrying

ser.close()