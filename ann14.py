# -*- coding: utf-8 -*-
"""ann14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a5ZQCC7Vdp7G6kBNkbDUenn3j6-2c-de
"""

import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import mnist
from PIL import Image

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalize pixel values to range [0, 1]

# Define the CNN model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_accuracy}')

# Load the custom input image
image = Image.open("test_)Pinp0.png")
image = image.resize((28, 28))
image = image.convert("L")
image = np.array(image) / 255.0

image = image.reshape((1, 28, 28, 1))

predictions = model.predict(image)

predicted_digit = np.argmax(predictions)

print("Predicted Digit:", predicted_digit)