---
title: Script guide

---

# Guide

## Project structure
```
.
└── 3d-recon/
    ├── apps/
    ├── scripts/
    ├── results/
    │   └── pifuhd_final/
    │       └── recon/
    ├── lightweight-human-pose-estimation.pytorch/
    ├── pifuhd/
    ├── checkpoints/
    └── venv/
```

## Script files
- `setup.sh`: remove files in input and output directory
- `sample_test.sh`: call `clean.sh`, `preprocess.sh` and `recon.sh` scripts, to quickly generate model.
- `clean.sh`: remove files in input and output directory
- `recon.sh`: start reconstruction in 256 resolution
- `hr_recon.sh`: start reconstruction in 512 resolution
- `preprocess.sh`: preprocess image in directory

## Applications
> Every scripts only accept image in `.png` or `.jpeg` formats
- `mesh_gen.py`
    - Generate meshes from given input images
    - Image must stored in folder in `--input-path` and must have `{image_name}_rect.txt` file that correspond to the image, in order to generate the mesh for that image.
    - Output of the script will store in
    - **Arguments**
        - `-r|--resolution`
            - If no value specified the default value will be 256
        - `-i|--input-path`
            - Path to input folder, All image in specified folder with correspond `_rect.txt` file will get process
            - If no value specified the default value will be `./sample_images`
- `rect_gen.py`
    - Generate `{image_name}_rect.txt` for every correspond image in specified folder
    - `_rect.txt` files are for storing crop position of the image
    - Format of `_rect.txt` files are `{x} {y} {image_width} {image_height}` where `{x}` and `{y}` can be both positive and negative integers.
    - `_rect.txt` files will generate in the `--input-path` folder.
    - **Arguments**
        - `-r|--resolution`
            - If no value specified the default value will be `1024`
        - `-i|--input-path`
        - `-f|--full-img`
            - determine whether `.rect.txt` will be the full image or not
            - If set to true image must be square.
    
- `preprocess.py`
    - Applies image processing to the image
    - **Arguments**
        - `-i|--input-path`
        - `-o|--output-path`
        Note: If input and output path are the same, processed images will override original images.