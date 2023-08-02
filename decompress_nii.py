import os
import shutil
import gzip

def decompress_files(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.nii.gz'):
                gz_file_path = os.path.join(root, file)
                nii_file_path = os.path.splitext(gz_file_path)[0]

                # Decompress the .nii.gz file to .nii
                with gzip.open(gz_file_path, 'rb') as f_in:
                    with open(nii_file_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)

                # Remove the .nii.gz file
                os.remove(gz_file_path)

if __name__ == "__main__":
    folder_path = "Test\ASNR-MICCAI-BraTS2023-SSA-Challenge-ValidationData"
    decompress_files(folder_path)
