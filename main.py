import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers
from tensorflow.keras.applications.xception import decode_predictions
from keras.models import Model

# Configura as imagens
data_directory_train = r'data\train'
data_directory_val = r'data\validation'
data_directory_test = r'data\test'
image_size = (224, 224)
input_shape = image_size + (3,)
use_data_augmentation = True
validation_split = 0.2
color_mode = "rgb"
classes = ['Ciclones', 'Oceano']

# Carregando os dados
train = tf.keras.preprocessing.image_dataset_from_directory(
    directory=data_directory_train,
    color_mode=color_mode,
    image_size=image_size,
    batch_size = 256
)

validation = tf.keras.preprocessing.image_dataset_from_directory(
    directory=data_directory_val,
    color_mode=color_mode,
    image_size=image_size,
    batch_size = 256
)

test = tf.keras.preprocessing.image_dataset_from_directory(
    directory=data_directory_test,
    color_mode=color_mode,
    image_size=image_size,
    batch_size = 256
)

def process(image, label):
    image = tf.cast(image / 255, tf.float32)
    return image, label

train = train.map(process)
validation = validation.map(process)
test = test.map(process)

# Mostrando as imagens
rows, columns = 2, 4
images, labels = list(*train.take(1))
plt.figure(figsize=(12, 6))

for i in range(rows * columns):
    plt.subplot(rows, columns, i + 1)
    plt.imshow(images[i])
    title = classes[int(labels[i])]
    plt.title(title)
    plt.axis('off')
plt.show()

rows, columns = 2, 4
images, labels = list(*validation.take(1))
plt.figure(figsize=(12, 6))

for i in range(rows * columns):
    plt.subplot(rows, columns, i + 1)
    plt.imshow(images[i])
    title = classes[int(labels[i])]
    plt.title(title)
    plt.axis('off')
plt.show()

# Data Augmentation

data_augmentation = tf.keras.Sequential([
  layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
  layers.experimental.preprocessing.RandomRotation(0.2),
])

rows, columns = 2, 4
images, labels = list(*validation.take(1))

plt.figure(figsize=(12, 6))
for images, labels in train.take(1):
    for i in range(rows * columns):
        augmented_images = data_augmentation(images)
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(augmented_images[0])
        plt.axis("off")

# Transfer Learning

pre_trained_model = tf.keras.applications.Xception(weights='imagenet',include_top=False, input_shape=(224, 224, 3))
pre_trained_model.trainable = False
pre_trained_model.summary()

for layer in pre_trained_model.layers[:]:
    layer.trainable = False

inputs = keras.Input(shape=(224, 224, 3))
x = pre_trained_model(inputs, training=False)
x = layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical")(x)
x = layers.experimental.preprocessing.RandomRotation(0.2)(x)
x = keras.layers.GlobalAveragePooling2D()(x)

outputs = keras.layers.Dense(2, activation="softmax")(x)
model = keras.Model(inputs, outputs)

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

history = model.fit(train, validation_data = validation, epochs=10)

# Gráficos
# Accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Predições
rows, columns = 2, 4
images, labels = list(*test.take(1))
plt.figure(figsize=(12, 6))
plt.subplots_adjust(hspace=0.7)
predictions = model.predict(images)

for i in range(rows * columns):
    plt.subplot(rows, columns, i + 1)
    plt.imshow(images[i])
    title = '\n'.join([f'{classes[j]} = {predictions[i][j] * 100:.2f}%' for j in range(len(classes))])
    plt.title(title)
    plt.axis('off')
plt.show()