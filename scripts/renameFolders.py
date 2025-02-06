import os

folder_path = 'F:/to sort'

def rename(folder_path):
    for folder_name in os.listdir(folder_path):
        old_name = os.path.join(folder_path, folder_name)
        new_name = os.path.join(folder_path, folder_name.replace(' ','-'))

        if os.path.isdir(old_name) and old_name != new_name:
            os.rename(old_name, new_name)
            print(f"Renamed '{folder_name}' to '{folder_name.replace(' ','-')}'")

rename(folder_path)