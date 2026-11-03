# PyTorch Projects

## Overview

This directory contains a collection of practical Deep Learning and Machine Learning projects developed using **Python and PyTorch**.

The purpose of these projects is to apply the theoretical concepts learned throughout the PyTorch learning journey and develop practical skills in building, training, evaluating, and deploying Neural Network models.

Projects are organized from beginner to advanced levels, covering Regression, Classification, CNNs, RNNs, LSTMs, Custom Neural Networks, and Medical Image Segmentation.

The ultimate goal is to develop a strong practical understanding of PyTorch through hands-on implementation and experimentation.

## Learning Objectives

Through these projects, I aim to:

- Apply PyTorch fundamentals to real-world problems.
- Implement different Neural Network architectures.
- Understand complete Deep Learning training pipelines.
- Work with different datasets and preprocessing techniques.
- Implement custom CNN architectures.
- Explore sequential data modeling using LSTM.
- Apply Transfer Learning and model optimization techniques.
- Develop Medical Image Segmentation models.
- Evaluate models using appropriate performance metrics.
- Build reproducible Deep Learning experiments.

## Project Roadmap

### 01. Linear Regression

**Objective:** Implement a Linear Regression model using PyTorch to understand the fundamentals of regression and parameter optimization.

**Topics Covered:**
- Linear Regression
- Weight and Bias
- Forward Propagation
- Mean Squared Error (MSE)
- Gradient Descent
- Backpropagation
- Model Training and Evaluation

### 02. Binary Classification

**Objective:** Build a Neural Network for binary classification using PyTorch.

**Topics Covered:**
- Binary Classification
- Artificial Neural Network (ANN)
- Sigmoid Activation Function
- Binary Cross Entropy Loss
- Optimizers
- Training and Validation
- Accuracy, Precision, Recall, and F1-Score

### 03. MNIST Classification

**Objective:** Develop a Neural Network to classify handwritten digits from the MNIST dataset.

**Topics Covered:**
- MNIST Dataset
- Image Preprocessing
- DataLoader
- Multilayer Perceptron (MLP)
- Softmax and Cross Entropy Loss
- Model Training
- Classification Evaluation
- Prediction Visualization

### 04. CNN Image Classification

**Objective:** Build a Convolutional Neural Network to classify images using PyTorch.

**Topics Covered:**
- Image Loading and Preprocessing
- Convolutional Layers
- Filters and Kernels
- Pooling Operations
- Activation Functions
- Batch Normalization
- Dropout
- CNN Training and Evaluation

### 05. LSTM Prediction

**Objective:** Develop an LSTM-based model to learn sequential patterns and perform prediction tasks.

**Topics Covered:**
- Sequential Data
- Recurrent Neural Network (RNN)
- Long Short-Term Memory (LSTM)
- Hidden State and Cell State
- Sequence Preparation
- Sliding Window Technique
- Time-Series Prediction
- Model Evaluation

### 06. Custom CNN

**Objective:** Design and implement a custom CNN architecture from scratch and evaluate its performance.

**Topics Covered:**
- Custom CNN Architecture
- Convolutional Blocks
- Activation Functions
- Pooling Layers
- Batch Normalization
- Dropout
- Weight Initialization
- Optimizer Comparison
- Hyperparameter Tuning
- Model Performance Evaluation

### 07. Brain Tumor Segmentation

**Objective:** Develop Deep Learning models for brain tumor segmentation using multimodal MRI data.

**Topics Covered:**
- Medical Image Analysis
- Brain MRI Preprocessing
- Multimodal MRI
- Image Segmentation
- U-Net Architecture
- U-Net++ Architecture
- Custom Segmentation Models
- Dice Loss
- Dice Score and IoU
- Hausdorff Distance (HD95)
- Model Comparison and Evaluation

## Project Structure

```text
projects/
│
├── README.md
│
├── 01_linear_regression/
│   ├── README.md
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── 02_binary_classification/
│   ├── README.md
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── 03_mnist_classification/
│   ├── README.md
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── 04_cnn_image_classification/
│   ├── README.md
│   ├── models/
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── 05_lstm_prediction/
│   ├── README.md
│   ├── models/
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── 06_custom_cnn/
│   ├── README.md
│   ├── models/
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
└── 07_brain_tumor_segmentation/
    ├── README.md
    ├── dataset/
    ├── models/
    ├── train.py
    ├── evaluate.py
    └── predict.py
```

*Note: Additional files and directories may be added depending on the requirements of each project.*

## Technologies & Libraries

- Python
- PyTorch
- Torchvision
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- OpenCV
- Pillow (PIL)
- MONAI
- NiBabel

## Development Workflow

Each project will follow a structured Deep Learning development workflow:

1. Problem Definition
2. Dataset Collection and Preparation
3. Data Preprocessing
4. Model Architecture Design
5. Loss Function Selection
6. Optimizer Selection
7. Model Training
8. Validation and Evaluation
9. Performance Analysis
10. Model Saving and Prediction

## Evaluation Metrics

Depending on the project, different evaluation metrics will be used.

| Task | Evaluation Metrics |
|---|---|
| Regression | MSE, MAE, RMSE, R² |
| Binary Classification | Accuracy, Precision, Recall, F1-Score, ROC-AUC |
| Image Classification | Accuracy, Precision, Recall, F1-Score |
| Time-Series Prediction | MAE, MSE, RMSE |
| Image Segmentation | Dice Score, IoU, HD95 |

## Learning Philosophy

- Start with simple models and gradually move toward advanced architectures.
- Understand the mathematics behind each implementation.
- Write PyTorch code from scratch whenever practical.
- Experiment with different architectures and optimizers.
- Compare model performance under consistent experimental conditions.
- Maintain clean, reusable, and well-documented code.
- Focus on understanding rather than simply copying implementations.

## Final Goal

Build a comprehensive collection of PyTorch projects that demonstrates practical knowledge of Machine Learning, Deep Learning, Computer Vision, and Medical Image Analysis.

**From basic Neural Networks to advanced Medical Image Segmentation — learning PyTorch through practical implementation.**
