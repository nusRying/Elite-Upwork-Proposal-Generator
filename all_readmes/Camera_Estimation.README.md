name:	nusRying/Camera_Estimation
description:	
--
# Camera Estimation using Feature Matching

This project implements a camera pose estimation pipeline using ORB feature matching and Essential Matrix estimation.

## Setup

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the `main.py` script with two images:

```bash
python main.py --img1 "path/to/image1.jpg" --img2 "path/to/image2.jpg"
```

The script will:
1. Detect keypoints and descriptors in both images.
2. Match features using BFMatcher.
3. Estimate the Essential Matrix and recover the relative Pose (Rotation `R` and Translation `t`).
4. Save an image `output_matches.png` visualizing the inlier matches.
5. Print `R` and `t` to the console.

## Notes

- The intrinsic camera matrix `K` is approximated in `main.py`. For accurate results with real cameras, you should calibrate your camera and update `K` in `main.py`.

