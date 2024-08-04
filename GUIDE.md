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
- `setup.sh`: Download checkpoints.
- `clean.sh`: Removes files in input and output directories.
- `recon.sh`: Starts reconstruction in 256 resolution.
- `hr_recon.sh`: Start reconstruction in 512 resolution.
- `preprocess.sh`: Preprocesses images in directory.

## Applications
> Every script accept only images in `.png` or `.jpeg` formats.
- `mesh_gen.py`
    - Generate meshes from given input images.
    - Image must stored in a folder by `--input-path` and must have a corresponding `{image_name}_rect.txt` file to generate the mesh for that image.
    - The script's output of the script will store in [`results/pifuhd_final/recon/`](results/pifuhd_final/recon/)
    - **Arguments**
        - `-r|--resolution`
            - If no value is specified, the default value will be 256.
        - `-i|--input-path`
            - Path to input folder, All images in the specified folder with correspond `_rect.txt` file will be processed.
            - If no value specified, the default value will be `./sample_images`.
- `rect_gen.py`
    - Generates `{image_name}_rect.txt` files for every corresponding image in the specified folder
    - `_rect.txt` files store the crop position of the image.
    - The format of `_rect.txt` files is `{x} {y} {image_width} {image_height}` where `{x}` and `{y}` can be positive and negative integers.
    - `_rect.txt` files will be generated in the folder specified by `--input-path`.
    - **Arguments**
        - `-r|--resolution`
            - If no value specified, the default value will be `1024`
        - `-i|--input-path`
            - If no value specified, the default value will be `./sample_image`
        - `-f|--full-img`
            - determine whether `.rect.txt` file will represent the full image.
            - If set to true, image must be square.
    
- `preprocess.py`
    - Applies image processing to the images.
    - If input and output path are the same, processed images will override original images.
    - **Arguments**
        - `-i|--input-path`
            - If no value specified, the default value will be `./sample_image`
        - `-o|--output-path`
            - If no value specified, the default value will be `./sample_image`

