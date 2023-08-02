# kaggle-empty-folder-fix
Fix the Kaggle empty file upload issue (e.g. nii.gz etc.) using this Python script.

## Description:
This repository provides a Python script to fix the issue of empty directories appearing when uploading MRI images and their respective masks in .nii.gz format on Kaggle. Kaggle's automatic unzipping of .nii.gz files results in empty folders displayed as directories in the Kaggle notebook. The script ensures that the .nii.gz files are correctly recognized, allowing smooth uploading and utilization of MRI data on Kaggle.

## Solution
The code decompresses .nii.gz files in the "SSA_Training" directory to .nii format and removes the original compressed files. It ensures that the MRI data is in a usable format for further analysis and processing.

## Dataset Structure:
<pre>
└───SSA_Training
│   │
│   └───BraTS-SSA-00002-000
│   │       BraTS-SSA-00002-000-seg.nii.gz
│   │       BraTS-SSA-00002-000-t1.nii.gz
│   │       ...
│   │
│   └───BraTS-SSA-00007-000
│   │       BraTS-SSA-00007-000-seg.nii.gz
│   │       BraTS-SSA-00007-000-t1.nii.gz
│   │       ...
│   │
│   └───BraTS-SSA-00008-000
│   │       BraTS-SSA-00008-000-seg.nii.gz
│   │       BraTS-SSA-00008-000-t1.nii.gz
│   │       ...
│   │
│   └───...
</pre>

## Code Summary: Decompress .nii.gz Files
1. Import the required modules: os, shutil, and gzip.
2. Define the decompress_files function that takes the folder_path as input.
3. Traverse through all files and subdirectories using os.walk.
4. Check if the file has the extension .nii.gz.
5. Decompress the .nii.gz file to .nii format.
6. Remove the .nii.gz file to avoid duplication.
7. Set the folder_path to "SSA_Training".
8. Call the decompress_files function to process the MRI data.

## Usage:

Clone the repository to your local machine:
<pre>
  python decompress_nii.py
</pre>

## Contributing:
Contributions to this repository are welcome. If you find any issues or have improvements to suggest, feel free to open an issue or create a pull request.

## Acknowledgments:
Special thanks to the BRATS2023 team for providing the dataset and Kaggle for hosting the platform to share and collaborate on data science projects.

## Disclaimer:
Please ensure that you have the necessary permissions to use the MRI dataset and always abide by the dataset's licensing terms and conditions.

## Author:
Hasan Nasir Khan (hasannasirk@gmail.com)

