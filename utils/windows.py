import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

def create_windows(subjects, dataset, window_size, time_step, enc_labels):
    # creo una lista delle possibili finestre che andranno convertite in immagini
    windows = []

    for subject in subjects:
        df_sub = dataset[dataset.id_subject == subject]
        indexes = df_sub.index
        for idx in range(indexes[0], indexes[-1]-window_size, time_step):
            try:
                win_labels = np.unique(
                    df_sub.loc[idx:idx+window_size, 'label_original'])
                if len(win_labels) == 1:
                    windows.append((subject, idx, enc_labels[win_labels[0]]))
            except:
                pass
    return np.array(windows)

def split_train_test_val(win_array, train_size=0.7, test_size=0.2, seed=None):
    assert(train_size+test_size<=1.0)
    sss1 = StratifiedShuffleSplit(n_splits=1, train_size=train_size, random_state=seed)
    train_index, rest_index = next(sss1.split(win_array[:, :2], win_array[:,2]))
    sss2 = StratifiedShuffleSplit(n_splits=1, train_size=test_size/(1.0-train_size),
                                      random_state=seed)
    test_index, val_index = next(sss2.split(
        win_array[rest_index, :2], win_array[rest_index, 2]))
    return win_array[train_index], win_array[rest_index][test_index], win_array[rest_index][val_index]