name:	nusRying/Hand_Tracking_Optical_Flow
description:	
--
# Hand Tracking using Optical Flow

Track hand motion using Sparse (Lucas-Kanade) and Dense (Farneback) Optical Flow.

## Setup
1. Install requirements:
`pip install -r requirements.txt`

## Usage

1. **Sparse Tracking (Lucas-Kanade)**:
   `python sparse_tracking.py`
   - Tracks specific feature points.
   - Good for tracking fingertips or knuckles.

2. **Dense Tracking (Farneback)**:
   `python dense_tracking.py`
   - Computes flow for every pixel.
   - Visualizes motion magnitude and direction with color.

