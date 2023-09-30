import tensorflow as tf
import numpy as np

def get_model(input_dim, optimizer, learning_rate, n_classes, model_name="vgg", add_noise=False,
              stdev=0.1, seed=None, trainable=True):
    optimizers = {
        'AMSGrad':tf.keras.optimizers.Adam(learning_rate=learning_rate, amsgrad=True),
        'Adam': tf.keras.optimizers.Adam(learning_rate=learning_rate, amsgrad=False),
        'Nadam': tf.keras.optimizers.Nadam(learning_rate=learning_rate),
        'SGD': tf.keras.optimizers.SGD(learning_rate=learning_rate, momentum=0.9)
    }

    hidden_layer = {
      "resnet": 64,
      "vgg": 64
    }

    if seed is not None:
      np.random.seed(seed)
      tf.random.set_seed(seed)
    
    model = tf.keras.Sequential()

    if add_noise:
      model.add(tf.keras.layers.GaussianNoise(stddev=stdev))

    if model_name == "resnet":
      pretrained_resnet50 = tf.keras.applications.resnet50.ResNet50(
                include_top=False,
                weights='imagenet',
                input_shape=input_dim,
                pooling='max',
                classes=n_classes
                )
      if not trainable:
        for each_layer in pretrained_resnet50.layers:
          each_layer.trainable=False
      model.add(pretrained_resnet50)
    else:
      model.add(tf.keras.layers.Convolution2D(16, (3, 3), activation='relu', input_shape=input_dim))
#      model.add(tf.keras.layers.Convolution2D(16, (3, 3), activation='relu'))
      model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
      model.add(tf.keras.layers.Dropout(0.25))
      model.add(tf.keras.layers.Convolution2D(32, (3, 3), activation='relu'))
#      model.add(tf.keras.layers.Convolution2D(32, (3, 3), activation='relu'))
      model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
      model.add(tf.keras.layers.Dropout(0.25))


    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(hidden_layer[model_name], activation='relu'))
    model.add(tf.keras.layers.Dropout(0.25))
    model.add(tf.keras.layers.Dense(n_classes, activation='softmax')) #[0 2 3]

    model.compile(optimizers[optimizer], loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#    print('Neural Network Model Summary: ')
    print(model.summary())
#    print('------------------------------')
    
    return model