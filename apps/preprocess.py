from PIL import Image, ImageOps
import os
import argparse
from pathlib import Path
from rembg import new_session, remove

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_path', type=str, default='./sample_images/')
parser.add_argument('-o', '--output_path', type=str, default='./sample_images/')
parser.add_argument('-jpg', '--save_as_jpg', type=bool, default=False)
parser.add_argument('-bg', '--keeps_background', type=bool, default=False)
parser.add_argument('-c', '--background_color', type=str, default='808080ff')
args = parser.parse_args()

input_dir = args.input_path
output_dir = args.output_path
quality = 85
extensions = ('.jpg','.jpeg', '.png','.JPG', '.JPEG', '.PNG')


if os.path.samefile(input_dir, output_dir):
    print('\033[93mWarning: Input and Output path are setted to be the same. Original image might get overridden \033[0m')

if not args.keeps_background:
    bg_color = tuple(int(args.background_color[i:i+2], 16) for i in (0, 2, 4, 6))
    model_name = "u2net_human_seg"
    session = new_session(model_name)

# Loop through all the images in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is an image
    if filename.endswith(extensions):
       
        # Open the image and applies rotation
        image = Image.open(f'{input_dir}/{filename}')
        image = ImageOps.exif_transpose(image)

        # Remove background if needed
        if not args.keeps_background:
            image = remove(image, bgcolor=bg_color, session=session)

        if image.mode in ("RGBA", "P") and args.save_as_jpg:
            image = image.convert("RGB")

        # Compress the image and save it to the output directory
        f_name = Path(filename).stem
        image.save(f'{output_dir}/{f_name} {".jpg" if args.save_as_jpg else ".png"}', quality=quality)
        print(f'saved: {output_dir}/{f_name} {".jpg" if args.save_as_jpg else ".png"} ')
        

print('Done!')
