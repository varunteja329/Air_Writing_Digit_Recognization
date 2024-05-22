# Air Writing Digit Recognition

This project utilizes a gy-521 sensor mounted on a glove to recognize handwritten digits using machine learning algorithms, including Gradient Boosting Classifier, AdaBoost Classifier, Extra Gradient Boosting, and Random Forest Classifier.

## Overview

Air Writing Digit Recognition is a project aimed at recognizing handwritten digits by tracking hand movements using a gy-521 sensor mounted on a glove. This repository contains the code and resources required to train and deploy the machine learning models for digit recognition.

## Features

- Utilizes gy-521 sensor mounted on a glove for tracking hand movements.
- Machine learning algorithms for digit recognition, including Gradient Boosting Classifier, AdaBoost Classifier, Extra Gradient Boosting, and Random Forest Classifier.
- Custom dataset creation for training.

## Requirements

- Arduino Uno
- PCB board
- GY-521 sensor
- Python 3.x
- Libraries: TensorFlow, NumPy, scikit-learn
- PyCharm IDE

## Setup

1. Clone the repository:git clone https://github.com/your_username/air-writing-digit-recognition.git
   
2. Install the required libraries:pip install tensorflow numpy scikit-learn
   
3. Upload the Arduino code to the Arduino Uno connected with the PCB board and GY-521 sensor.

4. Train the machine learning models using PyCharm IDE and the provided dataset.

5. Run the prediction script to recognize digits in real-time.

## Usage

- Ensure that the gy-521 sensor mounted on the glove is properly connected to the Arduino Uno board.
- Run the prediction script `predict.py` using PyCharm IDE to start recognizing digits.
- Follow the instructions displayed on the screen for writing digits in the air.

## Process

1. Calibrate the gy-521 sensor using Arduino IDE.
2. Collect data for digits 0-9 using the sensor mounted on the glove.
3. Perform data processing and feature extraction using PyCharm IDE.
4. Train the machine learning models: Gradient Boosting Classifier, AdaBoost Classifier, Extra Gradient Boosting, and Random Forest Classifier.
5. Evaluate the models and obtain accuracy metrics.

## Dataset

The dataset used for training the machine learning models is collected using the gy-521 sensor mounted on the glove. It consists of samples of handwritten digits drawn in the air.

## Models

The machine learning models used for digit recognition include:
- Gradient Boosting Classifier
- AdaBoost Classifier
- Extra Gradient Boosting
- Random Forest Classifier

These models are trained and evaluated using the provided dataset.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.












