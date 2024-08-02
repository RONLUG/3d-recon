import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-r', '--resolution', type=int, default=256)

args = parser.parse_args()

subprocess.run(['python', '-m', 'apps.rect_gen', '-r', '256', '--use_rect', '-i', image_path])
