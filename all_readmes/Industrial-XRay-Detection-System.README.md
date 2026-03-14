name:	nusRying/Industrial-XRay-Detection-System
description:	
--
# Industrial X-Ray Foreign Object Detection System

This project is a real-time industrial inspection system developed in MATLAB App Designer. It is designed to detect foreign objects in items (referred to as "plates" or "panels") passing through an X-ray scanner on a conveyor belt.

## ≡ƒÜÇ Overview

The system captures high-resolution video from a specialized video grabber, processes the frames to isolate the object of interest, and applies advanced image analysis to identify contamination or foreign objects. When a defect is detected, the system automatically triggers hardware signals to stop the conveyor and alert operators.

## Γ£¿ Key Features

- **Real-time Image Processing**: High-speed filtering and analysis loop for continuous inspection.
- **Advanced Contaminant Detection**:
  - Color-based "Erde" (Earth/Soil) filtering.
  - Morphological blob analysis to distinguish between expected item density and foreign materials.
  - Automatic bounding box and centroid calculation for detected objects.
- **Hardware Integration**:
  - **NI-DAQ Support**: Direct control of conveyor systems and alarms via National Instruments DAQmx.
  - **Watchdog Timer**: Ensures system reliability and hardware synchronization.
- **Automated Logging**:
  - Categorized storage of "Good" and "Bad" items.
  - Integration with Google Drive for remote monitoring.
  - Local backup system for data redundancy.
- **Interactive GUI**:
  - Live X-ray feed preview.
  - Processed image views (Processed Panel, Foreign Object Mask).
  - Sensitivity controls and real-time status indicators.

## ≡ƒ¢á Tech Stack

- **Language**: MATLAB
- **Framework**: MATLAB App Designer
- **Hardware Interface**: NI-DAQmx (Digital I/O)
- **Image Processing**: MATLAB Image Processing Toolbox
- **External Dependencies**:
  - `epiphan-usb-pci-drivers` (for video acquisition)
  - `ni-daqmx` (for hardware control)
  - `BellSound.wav` / `ac-bel-105874.mp3` (for audible alerts)

## ≡ƒôü Project Structure

- `XrayGUI_V4_1X.mlapp`: The main application file containing the UI and business logic.
- `XRAY.docx`: Technical documentation and requirement specifications.
- `epiphan-usb-pci-drivers/`: Drivers for the video capture hardware.
- `ni-daqmx_25.5_online.exe`: Installer for National Instruments hardware support.
- `XRAY.zip` / `XRAY1.rar`: Archived versions of the project assets.

## ΓÜÖ∩╕Å How it Works

1. **Initialization**: The system connects to the NI-DAQ hardware and localizes the video source.
2. **Calibration**: Standard density levels for "Good" plates are analyzed to set detection thresholds.
3. **Capture & Pre-process**: `getsnapshot` retrieves frames which are then cropped, filtered for noise, and adjusted for contrast.
4. **Segmentation**: The system identifies the plate boundaries and extracts the region of interest.
5. **Detection**: Any pixels falling outside the "normal" density range (after filtering out organic materials) are flagged as foreign objects.
6. **Action**: If a foreign object exceeds the size threshold:
   - Conveyor `STOP` signal is sent.
   - Alarm audio is played.
   - Current frame is saved to the `Bad` folder with a timestamp.

## ≡ƒô¥ Usage

1. Open `XrayGUI_V4_1X.mlapp` in MATLAB (R2022a or later recommended).
2. Ensure NI-DAQ hardware is connected and configured as `Dev1`.
3. Press **Start** to begin the inspection loop.
4. Adjust sensitivity and size thresholds as needed via the UI (if enabled).
5. Press **Stop** to safely terminate the session and reset hardware hooks.

---

_Note: This project is currently undergoing optimization to improve cycle time and processing efficiency._

