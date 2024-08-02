import os
import sys
import matplotlib.pyplot as plt
import torch
import cv2
import numpy as np
import subprocess
from os.path import dirname, abspath, join
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-r', '--resolution', type=int, default=256)

args = parser.parse_args()

current_dir = os.getcwd()
sys.path.append(current_dir)
image_path = current_dir + '/sample_images/'

subprocess.run(['python', '-m', 'pifuhd.apps.simple_test', '-r', str(args.resolution), '--use_rect', '-i', image_path])

