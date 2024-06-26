"""
    clean all classes repositories.
"""

import os

def del_data(this_dir):
    for source_dir in os.listdir():
        if not os.path.isdir(source_dir):
                continue
        if source_dir.startswith('.'):
            continue
        for class_name in os.listdir(source_dir):
            class_path = os.path.join(source_dir, class_name)
            if not os.path.isdir(class_path):
                continue

            for class_image in os.listdir(class_path):
                class_image_path = os.path.join(class_path, class_image)
                if os.path.isfile(class_image_path):
                    if class_image_path.endswith(('.jpg', '.jpeg', '.png')):
                        os.remove(class_image_path)

this_dir = '/home/cesar/Projects/RobosVGG116'

del_data(this_dir)