name:	nusRying/ComfyUI-Turbo-Portrait-Pipeline
description:	
--
# ComfyUI Turbo Portrait Pipeline ≡ƒÜÇ

[![ComfyUI](https://img.shields.io/badge/ComfyUI-Workflow-blueviolet)](https://github.com/comfyanonymous/ComfyUI)
[![SDXL](https://img.shields.io/badge/Model-SDXL-green)](https://stability.ai/)
[![RunPod](https://img.shields.io/badge/Platform-RunPod-orange)](https://www.runpod.io/)

Experience **ultra-fast**, high-fidelity AI portrait generation with **perfect face consistency**. This ComfyUI workflow is optimized for production environments, bringing generation times down from minutes to seconds.

## ≡ƒîƒ Key Features

-   **Consistent Identity**: Leverages **InstantID** and **IP-Adapter FaceID PlusV2** to maintain character likeness across every generation.
-   **RunPod Serverless Ready**: Fully compatible with RunPod serverless endpoints via API-format JSON.
-   **Memory Efficient**: Optimized for consumer hardware (4GB VRAM+) using `VAEDecodeTiled`.
-   **High Performance**: Tuned for speed (15-30s inference) without sacrificing 1024x1024 resolution.
-   **Dynamic Expressions**: Advanced prompt engineering hooks for varying character moods and poses.

---

## ≡ƒ¢á∩╕Å Optimization Breakdown

| Feature | Before | After (Optimized) |
| :--- | :--- | :--- |
| **Inference Speed** | ~120 Seconds | **15 - 30 Seconds** |
| **VRAM Peak** | >6 GB | **< 4 GB** |
| **Face Likeness** | Standard IP-Adapter | **InstantID + FaceID V2** |
| **Resolution** | 1024x1024 | 1024x1024 (Tiled) |

---

## ≡ƒÜÇ Getting Started

### 1. Requirements

You will need the following custom nodes installed:
- [ComfyUI-IPAdapter-Plus](https://github.com/cubiq/ComfyUI_IPAdapter_Plus)
- [ComfyUI-InstantID](https://github.com/ZHO-ZHO-ZHO/ComfyUI-InstantID)
- [InsightFace](https://github.com/deepinsight/insightface)

### 2. Models
Download and place the following in your `models/` folder:
- **Base**: `sd_xl_base_1.0.safetensors`
- **IP-Adapter**: `ip-adapter-faceid-plusv2_sdxl.bin`
- **CLIP Vision**: `CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors`

### 3. Usage
1. Import `workflow_api.json` into your ComfyUI interface.
2. Load your reference face image into the `Load Source Portrait` node.
3. Update the `Positive Prompt` with your desired expression/setting.
4. Click **Queue Prompt**.

---

## ≡ƒîÉ RunPod Deployment

This repository includes `workflow_api.json` specifically formatted for RunPod serverless workers. Use this with the [RunPod ComfyUI Worker](https://github.com/runpod-workers/worker-comfyui) for massive scalability.

## ≡ƒôä License
MIT License. Feel free to use in your SaaS platforms and commercial projects.

