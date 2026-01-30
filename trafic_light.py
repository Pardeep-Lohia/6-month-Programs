import cv2
import time
import numpy as np
from ultralytics import YOLO
import csv
# VIDEO PATH
VIDEO_PATH = "C:\\Users\\Pardeep\\Downloads\\videoplayback (1).mp4"

video = cv2.VideoCapture(VIDEO_PATH)
if not video.isOpened():
    print("Error: Unable to open video source")
    exit()

# YOLO MODEL
model = YOLO("yolov8n.pt")

WIDTH, HEIGHT = 640, 480

bottom_left  = (int(WIDTH * 0.05), int(HEIGHT * 0.95))
bottom_right = (int(WIDTH * 0.95), int(HEIGHT * 0.95))
top_right    = (int(WIDTH * 0.85), int(HEIGHT * 0.20))
top_left     = (int(WIDTH * 0.35), int(HEIGHT * 0.20))

roi_points = np.array([[bottom_left, top_left, top_right, bottom_right]], dtype=np.int32)

roi_mask = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)
cv2.fillPoly(roi_mask, roi_points, 255)

count_line_y = int(HEIGHT * 0.60)


vehicle_count = 0
# "car", "motorcycle", "bus", "truck"
car_count = 0
motorcycle_count = 0
bus_count = 0
truck_count = 0
prev_positions = {}  
speed_dict = {}      

PIXEL_TO_METER = 0.5   


counted_ids = set()

frame_index = 0


while True:
    ret, frame = video.read()
    if not ret or frame is None:
        print("End of video.")
        break

    frame_index += 1
    current_time = time.time()

    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    display_frame = frame.copy()


    cv2.polylines(display_frame, roi_points, True, (0, 255, 255), 2)


    cv2.line(display_frame, (0, count_line_y), (WIDTH, count_line_y), (0, 0, 255), 2)


    roi_frame = cv2.bitwise_and(frame, frame, mask=roi_mask)

    results = model.track(
        roi_frame,
        persist=True,
        conf=0.4,
        iou=0.5,
        verbose=False,
        tracker="bytetrack.yaml"
    )

    for r in results:
        if r.boxes.id is None:
            continue

        boxes = r.boxes.xyxy.cpu().numpy()
        ids = r.boxes.id.cpu().numpy()
        classes = r.boxes.cls.cpu().numpy()

        for box, track_id, cls_id in zip(boxes, ids, classes):
            label = model.names[int(cls_id)]

            if label in ["car", "motorcycle", "bus", "truck"]:
                x1, y1, x2, y2 = map(int, box)
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)

                speed_kmph = 0

                if track_id in prev_positions:
                    px, py, pt = prev_positions[track_id]
                    dist_pixels = np.sqrt((cx - px)**2 + (cy - py)**2)
                    time_diff = current_time - pt
# New Average=(A⋅N+x​)/N+1
                    if time_diff > 0:
                        dist_m = dist_pixels * PIXEL_TO_METER
                        speed_mps = dist_m / time_diff
                        speed_kmph = speed_mps * 3.6
                        if track_id in speed_dict:
                            old_avg = speed_dict[track_id]
                            new_avg = (old_avg * (len(speed_dict) - 1) + speed_kmph) / len(speed_dict)
                            speed_dict[track_id] = new_avg
                        else:
                            speed_dict[track_id] = speed_kmph
                        # speed_dict[label] = label

                prev_positions[track_id] = (cx, cy, current_time)

                
                cv2.rectangle(display_frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.circle(display_frame, (cx, cy), 4, (0,255,0), -1)

                speed_text = f"{int(speed_kmph)} km/h"
                label_text = f"ID {int(track_id)} {label}"

                cv2.putText(display_frame, label_text, (x1, y1 - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

                cv2.putText(display_frame, speed_text, (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

                if cy > count_line_y and track_id not in counted_ids:
                    vehicle_count += 1
                    if label == "car":
                        car_count+=1
                    if label == "motorcycle":
                        motorcycle_count+=1
                    if label == "bus":
                        bus_count+=1
                    if label == "truck":
                        truck_count+=1
                    counted_ids.add(track_id)

    cv2.putText(display_frame, f"Vehicle Count: {vehicle_count}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv2.putText(display_frame, f"car: {car_count} motorcycle: {motorcycle_count} bus: {bus_count} truck: {truck_count}",
                (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
    with open("vehicle_speeds.csv", "w", newline="") as csvfile:
         csvwriter = csv.writer(csvfile)
         csvwriter.writerow(["Vehicle ID", "Speed (km/h)"])
         for vid, speed in speed_dict.items():
               csvwriter.writerow([vid, f"{speed:.2f}"])

    cv2.imshow("Traffic CCTV - Speed Detection", display_frame)
    cv2.imshow("ROI Detection Area", roi_frame)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()









#  frame processing can be done here
# STEP 1: Frame Validation & Sync
# What it includes:
# Drop corrupted frames
# Handle missing frames
# Sync timestamp
# Why:
# CCTV streams often skip frames or lag.
# Module:
# OpenCV videoio
# System time utilities



#STEP 2: Resize & Aspect Normalization
# What it includes:
# Resize to standard resolution
# Maintain aspect ratio
# Why:
# AI models require fixed input size
# Processing becomes faster.
# Module:
# OpenCV imgproc


# STEP 3: Color Space Conversion
# What it includes:
# BGR → RGB
# BGR → Grayscale
# BGR → HSV
# Why:
# Different tasks need different color formats:
# Signal detection → HSV
# Edge detection → Grayscale
# DNN models → RGB
# Module:
# OpenCV imgproc



# STEP 4: Noise Reduction (Denoising)
# What it includes:
# Remove sensor noise
# Smooth compression artifacts
# Why:
# Noise reduces:
# Detection accuracy
# Tracking stability
# Module:
# OpenCV imgproc
# OpenCV photo

# STEP 5: Contrast & Brightness Correction
# What it includes:
# Histogram equalization
# Adaptive contrast enhancement
# Why:
# Traffic cameras suffer from:
# Glare
# Night darkness
# Fog
# Module:
# OpenCV imgproc
# OpenCV photo



# STEP 6: Shadow & Glare Handling
# What it includes:
# Suppress moving shadows
# Reduce headlight glare
# Why:
# Shadows can be mistaken as vehicles or motion.
# Module:
# OpenCV imgproc
# OpenCV bgsegm (extra)
# STEP 7: Region of Interest (ROI) Masking
# What it includes:
# Crop only road area
# Ignore sky, footpaths, buildings
# Why:
# Less image =
# ✔ Faster processing
# ✔ Fewer false detections
# Module:
# OpenCV core
# OpenCV imgproc

# 🟢 STEP 8: Perspective & Camera Correction
# What it includes:
# Lens distortion removal
# Perspective transformation
# Why:
# Needed for:
# Accurate distance
# Speed calculation
# Module:
# OpenCV calib3d
# 🟢 STEP 9: Background Modeling (Optional but Powerful)
# What it includes:
# Learn static background
# Isolate moving vehicles
# Why:
# Reduces AI workload by:
# Focusing only on moving objects
# Module:
# OpenCV video
# OpenCV bgsegm
# 🟢 STEP 10: Frame Selection / Skipping
# What it includes:
# Process every Nth frame
# Adaptive frame rate
# Why:
# Full AI on every frame is expensive.
# Module:
# System logic + videoio
