
# EMG Gesture Recording Starter Kit

This kit helps you record EMG data for 3 gestures using Arduino and Python.

## ✅ What’s Included

- `rest_data.csv`, `index_finger_data.csv`, `okay_data.csv`: Sample gesture datasets
- `record_emg.ino`: Arduino sketch to stream EMG data
- `record_emg.py`: Python script to log data from Arduino to CSV

## 🎓 Your Task

1. Connect 2 sEMG sensors to Arduino:
   - Channel 1 → A0
   - Channel 2 → A1
2. Upload `record_emg.ino` to Arduino.
3. Run `record_emg.py` from your computer.
4. Change `GESTURE_LABEL` to the gesture name you're recording.
5. Collect 60 seconds of data for each gesture.

Repeat for:
- rest
- index_finger
- okay

## 📂 Output Format

Each CSV will have:
```
ch1, ch2, timestamp_ms, label
523, 478, 100, rest
```

## 🧪 Test Before Recording

Use the sample datasets to test your segmentation, feature extraction, and modeling code.

Happy coding!
