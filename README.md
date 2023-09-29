# Overview
The UniProt Structures Parser repository contains Python scripts and a Jupyter notebook designed to parse and process protein structure data from UniProt. The repository focuses on handling CIF (Crystallographic Information File) format files and converting sequences to SDF (Structure Data File) format.

# Installation
To use the repository, clone it to your local machine using the following command:
```git clone https://github.com/f-normies/UniProt_structures_parser.git```

# Files setup

## 1. run_scripts.bat
A batch file designed to run multiple Python scripts sequentially. It sets up various paths and runs `MergePDB.py`, `SeqToSDF.py`, and `UniquifySDF.py` with the necessary arguments.

### Setup
- Place this batch file in the directory where your Python scripts are located.
- Modify the paths for `DATA_DIR`, `INPUT_FILE`, `PROCESSED_FILE`, `SDF_FILE`, `UNCHARGED_SDF_FILE`, and `CONFIG_FILE` according to your directory structure.

## 2. config.json
A configuration file containing settings for Python scripts.

### Setup
- Modify the paths for `"input"` and `"output"` according to your directory structure.
- Adjust other parameters like `"column"`, `"charged"`, `"alphabet"`, `"threads"`, `"separator"`, `"filename"`, and `"delete_tmp"` based on your preferences.

## 3. cif_parser.ipynb
A Jupyter notebook for parsing CIF files.

### Setup
- Ensure all required libraries (`requests`, `pandas`, `Bio.PDB`) are installed.
- Modify the paths specified in the main execution section of the script, such as `save_cif_path` and the path to the input dataset, to match your directory structure and dataset location.
- Adjust the parameters in the main execution section, such as the `number of cores` and the `number of files to process`, based on your system's capabilities and your specific requirements.