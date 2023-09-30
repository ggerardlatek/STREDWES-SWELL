# Training and Testing model on Swell dataset (Google Colaboratory) 

## Set-up Google Colab

- Choose the Google Colab Runtime
  - Click the “Runtime” dropdown menu
  - Select “Change runtime type”
  - Select python3 and GPU as hardware accelerator
- Place the processed dataset, `dataset_swell_processed.pkl`, in the `dataset` folder.

  **Note**: A copy of this processed dataset is already available from the repository.

## Training and test

- Open the notebook `train_test.ipynb`
- Run all the cells

The notebook trains a model training for each subject.

Confusion matrices and test accuracies are computed for all subjects (label 0: no stress class; label 1 - stress class).

The final results `results_swell.pkl` is stored in the `results` folder.
