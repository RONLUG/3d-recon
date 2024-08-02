import os

current_dir = os.getcwd()
dir_name = 'results/pifuhd_final/recon'
files = os.listdir(dir_name)
delete_file_types = ('.png', '.obj')

for file in files:
    if file.endswith(delete_file_types):
        os.remove(os.path.join(dir_name, file))
        print(f'removed: {file}')
