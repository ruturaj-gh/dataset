import os

def rename_images(folder_path, prefix):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file and rename it
    for i, file in enumerate(files):
        # Check if the file is an image (you can add more conditions based on your needs)
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Form the new filename using the specified prefix and index
            new_name = f'{prefix}_{i+1}.png'
            
            # Construct the full paths for the old and new names
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)

# Replace 'your_folder_path' with the path to your folder containing images
# Replace 'new_prefix' with the desired prefix for the new filenames
rename_images('./', 'Te-pi')
