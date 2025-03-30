import cv2
import torch
import numpy as np
from ultralytics import YOLO
from tkinter import Tk, filedialog
import os

# Open file dialog
Tk().withdraw()  
video_path = filedialog.askopenfilename(title="Select a Basketball Video", filetypes=[("All Files", "*.*")])
if not video_path:
    print("No video selected. Exiting.")
    exit()

#pretrained model
model = YOLO('best.pt')

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Tracking variables
total_shots = 0
made_shots = 0
ball_positions = []
prev_shot_detected = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    results = model(frame)
    detections = results[0].boxes.data.cpu().numpy() if results and results[0].boxes is not None else []
    
    ball_detected = False
    hoop_detected = None
    
    for det in detections:
        x1, y1, x2, y2, conf, cls = det[:6] 
        
        if conf < 0.2:  
            continue
        
        if int(cls) == 0:  
            ball_detected = True
            ball_positions.append(((x1 + x2) / 2, (y1 + y2) / 2))
            cv2.circle(frame, (int((x1 + x2) / 2), int((y1 + y2) / 2)), 5, (0, 255, 0), -1)
        elif int(cls) == 1:  
            hoop_detected = ((x1 + x2) / 2, (y1 + y2) / 2)
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
    
    if len(ball_positions) > 10:
        ball_positions.pop(0)
    
    # shot detection logic
    shot_detected = False
    if len(ball_positions) > 1 and hoop_detected:
        prev_x, prev_y = ball_positions[-2]
        curr_x, curr_y = ball_positions[-1]
        hoop_x, hoop_y = hoop_detected
        
        if prev_y < hoop_y and curr_y > hoop_y and abs(prev_x - hoop_x) < 30:
            shot_detected = True
            if not prev_shot_detected: 
                made_shots += 1
                total_shots += 1
    elif not ball_detected and prev_shot_detected:
        total_shots += 1
    
    prev_shot_detected = shot_detected
    
    cv2.putText(frame, f'Shots Made: {made_shots}/{total_shots}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Basketball Shot Tracker', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
