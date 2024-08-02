from PIL import Image, ImageOps
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_path', default='./sample_images/')
parser.add_argument('-o', '--output_path', default='./sample_images/')
args = parser.parse_args()

input_dir = args.input_path
output_dir = args.output_path
quality = 85
extensions = ('.jpg','.jpeg', '.png','.JPG', '.JPEG', '.PNG')


if os.path.samefile(input_dir, output_dir):
    print('\033[93mWarning: Input and Output path are setted to be the same. Image will be overridden \033[0m')

# Loop through all the images in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is an image
    if filename.endswith(extensions):
       
        # Open the image and applies rotation
        image = Image.open(f'{input_dir}/{filename}')
        image = ImageOps.exif_transpose(image)
        
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        # Compress the image and save it to the output directory
        image.save(f'{output_dir}/{filename}', quality=quality)
        print(f'saved: {output_dir}{filename}')
        

print('Done!')

