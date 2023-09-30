# Preprocessing

## Download the raw dataset

The raw dataset necessary to train and test Stredwes is available from
https://ssh.datastations.nl/dataset.xhtml?persistentId=doi:10.17026/dans-x55-69zp 

Two set of files are necessary:

1. All `.S00` files that contain the raw data with the Mobi signals that compose the dataset.
These are stored `0 - Raw Data/D - Physiology - raw data/Mobi signals _raw and filtered_` folder of the official site.

    To browse the folder and download the files, scroll to the bottom of the page and select the `Tree` button to the right of "Change View".

    **Note:** 
    > Due to the size of the dataset and number of files, it is not possible to download all files at once. It is possible to download selections. Please contact DANS via info@dans.knaw.nl when you wish to use all files.

2. A copy of `D - Physiology features (HR_HRV_SCL - final).csv` file, downloaded from the folder `3 - Feature Dataset/per sensor` of the official site, which is already in the `raw_data` folder of this repository.

## Convert the raw Mobi signals
    
### Convert S00 to mat files

**Note:** You will need access to a MATLAB environment to perform the format conversion.

Inside the `convert_S00_files` folder, there is a processing pipeline to convert `.S00` raw file to `.mat` files. To run the pipeline follow these steps:

1. Move all downloaded `.S00` raw data files in the `convert_S00_files/Swell_DB_S00_raw` folder.

2. Run the MATLAB script `Reading_Swell_S00_file.m` to convert each `.S00` datafile to a corresponding `.mat` datafile.

The `.mat` files will be stored in the `dataset` folder. 
    
## Preprocessing
    
Open in Google Colab the notebook 'preprocessing.ipynb' and run all cells.

The final processed dataset `dataset_swell_processed.pkl` is located into the `dataset` folder.







