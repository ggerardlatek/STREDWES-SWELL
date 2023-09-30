from subprocess import call
call("pip install awscli".split(" "))
call("pip install opencv-python".split(" "))

#Download e installazione del nuovo package "pyts" da s3
call("aws s3 sync s3://stress-detection-datasets/Swell_dataset_mat_raw/pyts_package_modified ./pyts_package_modified".split(" "))
call("python -m pip install -e pyts_package_modified".split(" ")) 

import numpy as np
import pandas as pd
import cv2 as cv
import math
from tensorflow.keras.utils import Sequence
from pyts_package_modified.pyts.image import RecurrencePlot     
     

class RPGenerator(Sequence):
    def __init__(self,
        dataset,
        windows,
        features,
        batch_size=64,
        image_size=128,
        window_size=60 * 35,
        RP_distance='euclidea',
        shuffle=True,
        seed=None):
      
        if seed is not None:
            np.random.seed(seed)
        # carico i dati dei soggetti specificati
        self.dataset = dataset
        self.features = features
        self.window_size = window_size
        self.image_size = image_size
        self.RP_distance = RP_distance
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.rp = RecurrencePlot()  #threshold='point', percentage=20 da valutare questi parametri
       
        # creo una lista delle possibili finestre che andranno convertite in immagini
        self.windows = windows
                  
        self.on_epoch_end()
    
    def on_epoch_end(self):
        if self.shuffle:
            np.random.shuffle(self.windows)

    def get_labels(self):
        return self.windows[:,2]
            
    def get_image(self, subject, i):
        current_window = self.dataset[self.dataset.id_subject==subject].\
            loc[i:i+self.window_size-1, self.features].to_numpy().T
        #Resizing 
        rp_i=self.rp.transform(current_window, dist_name=self.RP_distance) 
        rp_ires=np.empty([len(self.features),self.image_size, self.image_size])
        for c in range(0, np.shape(rp_i)[0]):  # itero le immagini (n° channels)
            rp_resized=cv.resize(rp_i[c], (self.image_size,self.image_size)) #,interpolation=cv.INTER_AREA  #cv.INTER_LANCZOS4 #cv.INTER_LINEAR (default) etc
            rp_ires[c] = rp_resized
        return np.transpose(rp_ires,(1,2,0))  #da (n°chan,dim,dim) a (dim,dim,n°chan)

    def __len__(self):
        return math.ceil(len(self.idx_list) / self.batch_size)

    def __getitem__(self, idx):
        batch = self.windows[idx * self.batch_size:(idx + 1) * self.batch_size]
        return np.array([self.get_image(subject, i) for subject, i, _ in batch]), batch[:,2]
