import os
from bing_images import bing

def ensure_images(class_path, class_name, target_num):
    existing_images = os.listdir(class_path)
    existing_count = len(existing_images)
    
    if existing_count >= target_num:
        print(f"Already have {existing_count} images for class: {class_name}")
        return

    remaining = target_num - existing_count
    print(f"Need {remaining} more images for class: {class_name}")

    queries = [class_name, f"{class_name} photos", f"{class_name} pictures", f"{class_name} images"]
    
    for query in queries:
        if remaining <= 0:
            break
        try:
            bing.download_images(query,
                                 limit=200,
                                 output_dir=class_path,
                                 pool_size=60,
                                 file_type="jpeg",
                                 force_replace=False)
            
            existing_count = len(os.listdir(class_path))
            remaining = target_num - existing_count
            print(f"Remaining images needed: {remaining}")
        except Exception as e:
            print(f"Error downloading images for query {query}: {e}")

def fill_data(source_dir, target_num=60):
    for class_name in os.listdir(source_dir):
        class_path = os.path.join(source_dir, class_name)
        if not os.path.isdir(class_path):
            continue

        os.makedirs(class_path, exist_ok=True)
        ensure_images(class_path, class_name, target_num)

source_directory = '../alldata'
fill_data(source_directory)
