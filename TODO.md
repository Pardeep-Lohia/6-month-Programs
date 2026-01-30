# TODO for Completing trafic_light.py

- [x] Add necessary imports (e.g., numpy)
- [x] Initialize background subtractor outside the loop
- [x] Define ROI mask outside the loop
- [x] In the loop, after frame read:
  - [x] Step 2: Resize frame to standard resolution (e.g., 640x480)
  - [x] Step 3: Convert to HSV color space
  - [x] Step 4: Apply noise reduction (GaussianBlur)
  - [x] Step 5: Apply contrast and brightness correction (histogram equalization on V channel)
  - [x] Step 6: Handle shadows and glare (morphological operations)
  - [x] Step 7: Apply ROI masking
  - [x] Step 8: Skip perspective correction for simplicity
  - [x] Step 9: Apply background modeling (subtract background)
  - [x] Step 10: Implement frame selection (process every 5th frame)
- [x] Update imshow to show processed frame
- [x] Test the script (run and check for errors)
