# Single view 3D reconstruction
This project focused on improving [PIFuHD](https://github.com/facebookresearch/pifuhd) reconstruction results by exploring PIFuHD and experimenting with preprocessing methods on input images to make them more suitable for reconstruction.


Basic preprocessing is handled in [`preprocess.sh`](./scripts/preprocess.sh), but additional preprocessing is recommended as needed for each image.

## Recommended preprocessing pipeline
![PIFuHD Image processing](./assets/image_processing_pipeline.svg)

## Quick start
**Requirements**: CUDA supported GPU
**Tested machine**: 
- **Graphic card**: NVIDIA GeForce GTX TITAN X
- **CPU**: Intel Core i7-5930k 
- **Ram**: 62GB
- **OS**: Ubuntu 22.04.4 LTS
- **CUDA**: v11.5
- **Python**: v3.10.12


**Clone repository**
```bash
git clone https://github.com/RONLUG/3d-recon.git
cd 3d-recon
git submodule update --init --recursive
```

**Setup environment**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Download pretrained models**
```bash
sh ./scripts/setup.sh
```

**Run sample test**
```bash
sh ./scripts/preprocess.sh
sh ./scripts/recon_gen.sh
```
> For more Information about custom input, script arguments, and recommended custom preprocessing you can read [this document](GUIDE.md)

## Suitable Input images for PIFuHD
- **Posture**
    - *A Pose* is the most effective for reconstruction
    - Keep fingers stick together or place hands inside pocket to avoid issue when generating individual fingers
- **Camera**
    - The optimal camera angle is parallel to the floor, with the camera positioned at the middle height of the model. A tilted camera might cause model to proportional inaccuracies.)
    - Images should have at least 2k resolution.
- **Scene**
    - Images taken in medium light environments usually gives the best results.
    - Avoid scenes with more than 1 person inside.
