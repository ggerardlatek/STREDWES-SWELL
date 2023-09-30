#from subprocess import call
#call("pip install pyts".split(" "))
# call("pip install delayed".split(" "))

import numpy as np
import pandas as pd
import math
from tensorflow.keras.utils import Sequence
from pyts.image import GramianAngularField

class GAFGenerator(Sequence):
    def __init__(self,
        dataset,
        windows,
        features,
        batch_size,
        image_size,
        method,
        window_size,
        shuffle=False,
        seed=None):
      
        if seed is not None:
            np.random.seed(seed)
            
        # carico i dati dei soggetti specificati
        self.dataset = dataset
        self.features = features
        self.window_size = window_size
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.gaf = GramianAngularField(image_size=image_size, sample_range=None, method=method)
        self.windows = windows
        
        self.on_epoch_end()
    
    def on_epoch_end(self):
        if self.shuffle:
            np.random.shuffle(self.windows)

    def get_labels(self):
        return self.windows[:,2]
            
    def get_image(self, subject, i):
        current_window = self.dataset[self.dataset.id_subject==subject].\
            loc[i:i+self.window_size-1, self.features].to_numpy().T #(4, 100254)(#channels, win=wsize*f) 
        return np.transpose(self.gaf.transform(current_window), (1, 2, 0)) #(83, 83, 4) (dimimg,dimimg,#channels)

    def __len__(self):
        return math.ceil(len(self.windows) / self.batch_size)

    def __getitem__(self, idx):
        batch = self.windows[idx * self.batch_size:(idx + 1) * self.batch_size]
        return np.array([self.get_image(subject, i) for subject, i, _ in batch]), batch[:,2]

    def __call__(self):
        return self
