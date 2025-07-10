
import serial
import time
import pandas as pd

# Set this to your COM port (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux)
SERIAL_PORT = 'COM3'
BAUD_RATE = 9600
DURATION = 60  # seconds
GESTURE_LABEL = 'index_finger'  # Change as needed

ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
time.sleep(2)

data = []
start_time = time.time()
print(f"Recording gesture: {GESTURE_LABEL}...")

while time.time() - start_time < DURATION:
    line = ser.readline().decode().strip()
    if line:
        try:
            ch1, ch2, ts = line.split(',')
            data.append([int(ch1), int(ch2), int(ts), GESTURE_LABEL])
        except ValueError:
            continue

df = pd.DataFrame(data, columns=["ch1", "ch2", "timestamp_ms", "label"])
df.to_csv(f"{GESTURE_LABEL}_data.csv", index=False)
print("Data saved successfully.")
