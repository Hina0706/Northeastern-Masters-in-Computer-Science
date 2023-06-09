import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
import os
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
import pathlib
from tensorflow.keras.models import load_model

def generate_zillow_inference():
    # Define the class names
    class_names = ['1000', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']

    # Reload a fresh Keras model from the saved model in directory
    new_model = tf.keras.models.load_model("C:\\Users\\Michael Mills\\Documents\\Final Project\\Saved_Models\\zillow_model")

    # Check its architecture
    new_model.summary()

    # Preprocess the input image
    def preprocess_image(image_path):
        img = image.load_img(image_path, target_size=(360, 360))
        img_array = image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create batch axis
        return img_array

    # Make a prediction using the loaded model
    def predict_image(image_path, model):
        img_array = preprocess_image(image_path)
        prediction = model.predict(img_array)
        return prediction

    # Specify the path to the input image
    image_path = "C:\\Users\\Michael Mills\\Documents\\Final Project\\Photos\\Zillow_Test_Photo\\test_photo.jpg"

    # Make a prediction using the loaded model
    prediction = predict_image(image_path, new_model)

    # Print the predicted class name and the corresponding probability
    predicted_class_index = np.argmax(prediction)
    predicted_class_name = class_names[predicted_class_index]
    print("Predicted class:", predicted_class_name)
    print("Probability:", prediction[0][predicted_class_index])


def main():
    generate_zillow_inference()

if __name__ == "__main__":
    main()
