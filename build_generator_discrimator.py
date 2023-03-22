def build_generator():
    model = Sequential()
    dropout = 0.4

    model.add(Dense(3*4*512, activation="relu", imput_dim=256))
    model.all(Reshape(3*4*512))
    model.add(Dropout(dropout))

    model.add(UpSampling2D())
    model.add(Conv2DTranspose(256,kernel_size=3,padding="same"))
    model.add(BatchNormalization(momentum=0.9))
    model.add(Activation("relu"))

    model.add(UpSampling2D())
    model.add(Conv2DTranspose(128,kernel_size=3,padding="same"))
    model.add(BatchNormalization(momentum=0.9))
    model.add(Activation("relu"))

    model.add(UpSampling2D())
    model.add(Conv2DTranspose(64,kernel_size=3,padding="same"))
    model.add(BatchNormalization(momentum=0.9))
    model.add(Activation("relu"))
   
    # Output resolution, additional upsampling
    model.add(UpSampling2D())
    model.add(Conv2DTranspose(1,kernel_size=3,padding="same"))
    model.add(Activation("tanh"))

    model.summary()

    return model


def build_discriminator():
    model = Sequential()
    image_shape = 64*16

    model.add(Conv2D(64, kernel_size=3, strides=2, input_shape=image_shape, 
                     padding="same"))
    model.add(LeakyReLU(alpha=0.2))

    model.add(Dropout(0.25)) #random set input to 0 prevent overfitting
    model.add(Conv2D(32, kernel_size=3, strides=2, padding="same"))
    model.add(BatchNormalization(momentum=0.8))
    model.add(LeakyReLU(alpha=0.2))

    model.add(Dropout(0.25))
    model.add(Conv2D(16, kernel_size=3, strides=2, padding="same"))
    model.add(BatchNormalization(momentum=0.8))
    model.add(LeakyReLU(alpha=0.2))

    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))

    model.summary()

    return model