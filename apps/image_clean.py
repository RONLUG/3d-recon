import os

dir_name = 'sample_images'
files = os.listdir(dir_name)
delete_file_types = ('.txt', '.jpeg', '.jpg', '.png', '.JPEG', '.JPG', '.PNG')

for file in files:
    if file.endswith(delete_file_types):
        os.remove(os.path.join(dir_name, file))
        print(f'removed {file}')
