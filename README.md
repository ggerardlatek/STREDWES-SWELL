# Stredwes for SWELL-KW

This repository contains supporting code to convert and preprocess the [SWELL-KW](https://ssh.datastations.nl/dataset.xhtml?persistentId=doi:10.17026/dans-x55-69zp) dataset raw data files and then train a model per each subject of the SWELL-KW [experiment](http://cs.ru.nl/~skoldijk/SWELL-KW/Dataset.html).

## Usage

### Google Colab

The code runs successfully in Google Colab.

There are two main notebooks

 - Preprocessing (Optional)
 
    [![Preprocessing](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggerardlatek/STREDWES-SWELL/blob/main/preprocessing.ipynb)

    For the preprocessing step to run successfully the original SWELL-KW dataset Mobi files with physiological signals must have been converted into MATLAB format.

    For instructions on how to conver the Mobi files to MATLAB format please refer to [Convert Mobi files](doc/preprocessing.md).

    The MATLAB format files must then be stored in the `raw_data` subfolder of your personal Google Drive top-level folder. This folder should be named `STREDWES-SWELL`.

 - Training
    
    [![Training](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggerardlatek/STREDWES-SWELL/blob/main/train_test.ipynb)

    For the notebook to run successfully the output of the preprocessing notebook must be stored under the `dataset` folder of the Google Runtime. A copy of this file is also uploaded to this GitHub repository.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License - see the [LICENSE](https://creativecommons.org/licenses/by-nc/4.0/) file for details.

## Acknowledgments

### References and citations

- Stress Detection from Wearable Sensor Data Using Gramian Angular Fields and CNN

    - **Authors:** Michela Quadrini, Sebastian Daberdaku, Alessandro Blanda, Antonino Capuccio, Luca Bellanova, Gianluca Gerard
    - **Conference:** Discovery Science
    - **Year:** 2022
    - **Publisher:** Springer Nature Switzerland
    - **Location:** Cham
    - **Pages:** 173-183
    - **ISBN:** 978-3-031-18840-4




