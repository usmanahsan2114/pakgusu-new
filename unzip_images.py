
import zipfile
import os

base_dir = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza\images\products\pass-through-chambers"
zip_files = {
    "BANNER & Pass-Through Chambers.zip": "banner-pass-through-chambers",
    "Chamber Variations.zip": "chamber-variations",
    "Key Features.zip": "key-features",
    "SEE IT IN ACTION.zip": "see-it-in-action"
}

def unzip_all():
    if not os.path.exists(base_dir):
        print(f"Base dir not found: {base_dir}")
        return

    for zip_name, content_folder in zip_files.items():
        zip_path = os.path.join(base_dir, zip_name)
        target_dir = os.path.join(base_dir, content_folder)
        
        if os.path.exists(zip_path):
            print(f"Unzipping {zip_name} to {target_dir}...")
            # Create target directory if it doesn't exist
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(target_dir)
                
                # Remove zip file after extraction
                os.remove(zip_path)
                print(f"Extracted and removed {zip_name}")
            except zipfile.BadZipFile:
                print(f"Error: {zip_name} is a bad zip file")
            except Exception as e:
                print(f"Error extracting {zip_name}: {e}")
        else:
            print(f"Zip file {zip_name} not found.")

if __name__ == "__main__":
    unzip_all()
