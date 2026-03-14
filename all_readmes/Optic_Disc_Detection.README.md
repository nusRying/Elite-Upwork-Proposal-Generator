name:	nusRying/Optic_Disc_Detection
description:	
--
# Optic Disc Detection (U-Net)

Deep learning pipeline for optic disc segmentation on retinal fundus images.

## Prerequisites

From repository root:

```bash
pip install -r Optic_Disc_Detection/requirements.txt
```

## Dataset Setup

1. Download DRIVE and place zip in `Optic_Disc_Detection/downloads/`.
2. Run:

```bash
python Optic_Disc_Detection/setup_dataset.py
```

Detailed instructions:

- `Optic_Disc_Detection/DATASET_DOWNLOAD.md`

## Training

```bash
python Optic_Disc_Detection/train.py --images_dir Optic_Disc_Detection/data/training/images --masks_dir Optic_Disc_Detection/data/training/masks --epochs 50 --batch_size 4
```

Best checkpoint is saved to `checkpoints/best_model.pth`.

## Evaluation

```bash
python Optic_Disc_Detection/evaluate.py --images_dir Optic_Disc_Detection/data/test/images --masks_dir Optic_Disc_Detection/data/test/masks --model_path checkpoints/best_model.pth
```

## Inference

```bash
python Optic_Disc_Detection/inference.py --image_path path/to/image.jpg --model_path checkpoints/best_model.pth --save
```

Output image is saved as `output_detection.png` when `--save` is used.

## Notes

- CLAHE preprocessing is applied in both dataset loading and inference.
- Use the same `--img_size` across training, evaluation, and inference for consistency.

