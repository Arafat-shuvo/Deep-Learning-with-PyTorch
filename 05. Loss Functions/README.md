
# 05. Loss Functions

## Overview

Loss Functions are essential components of Neural Network training. They measure the difference between a model's predictions and the actual target values.

In this chapter, we will explore different loss functions available in PyTorch, understand their mathematical foundations, and learn how to implement them using `torch.nn`.

The goal is to understand **how loss is calculated, when to use each loss function, and how to select the appropriate loss function for different machine learning tasks.**

## Learning Objectives

By completing this chapter, you will be able to:

- Understand what a Loss Function is and why it is important.
- Calculate prediction errors using different loss functions.
- Understand the mathematical equations behind each loss function.
- Implement loss functions using PyTorch.
- Identify the differences between regression and classification loss functions.
- Select an appropriate loss function based on the problem type.

## Topics Covered

### 1. Mean Squared Error (MSE)

- Introduction to Mean Squared Error.
- Mathematical formula of MSE.
- Understanding squared prediction errors.
- Implementing `nn.MSELoss()`.
- Practical examples using PyTorch.

### 2. Mean Absolute Error (MAE)

- Introduction to Mean Absolute Error.
- Mathematical formula of MAE.
- Understanding absolute prediction errors.
- Implementing `nn.L1Loss()`.
- Comparing MAE with MSE.

### 3. Binary Cross Entropy (BCE)

- Introduction to Binary Cross Entropy.
- Understanding binary classification loss.
- Mathematical formula of BCE.
- Understanding probability-based predictions.
- Implementing `nn.BCELoss()`.
- Practical binary classification examples.

### 4. BCEWithLogitsLoss

- Understanding Logits.
- Difference between Sigmoid and Logits.
- Introduction to `nn.BCEWithLogitsLoss()`.
- Why combining Sigmoid and BCE is numerically more stable.
- Implementing binary classification with logits.
- Comparing BCE and BCEWithLogitsLoss.

### 5. Cross Entropy Loss

- Introduction to Cross Entropy Loss.
- Understanding multiclass classification.
- Mathematical foundation of Cross Entropy.
- Understanding class probabilities and logits.
- Implementing `nn.CrossEntropyLoss()`.
- Understanding target labels and prediction shapes.
- Practical multiclass classification examples.

### 6. Loss Function Comparison

- MSE vs MAE.
- BCE vs BCEWithLogitsLoss.
- Binary Cross Entropy vs Cross Entropy Loss.
- Regression vs Classification Loss Functions.
- Comparing loss values using PyTorch.
- Selecting the appropriate loss function for different tasks.

## Technologies & Libraries

- Python
- PyTorch
- NumPy
- Matplotlib

## Folder Structure

```text
05. Loss Functions/
│
├── README.md
│
├── 01_Mean_Squared_Error/
│   └── mse_loss.py
│
├── 02_Mean_Absolute_Error/
│   └── mae_loss.py
│
├── 03_Binary_Cross_Entropy/
│   └── binary_cross_entropy.py
│
├── 04_BCEWithLogitsLoss/
│   └── bce_with_logits_loss.py
│
├── 05_Cross_Entropy_Loss/
│   └── cross_entropy_loss.py
│
└── 06_Loss_Function_Comparison/
    └── loss_comparison.py
```

## Learning Approach

Each topic will be implemented in a separate Python file.

For every loss function, we will:

1. Understand the mathematical concept.
2. Learn the mathematical formula.
3. Calculate loss manually using a small example.
4. Implement the loss function using PyTorch.
5. Analyze the output.
6. Compare its behavior with other loss functions.

## Expected Outcomes

After completing this chapter, you will be able to:

- Understand the mathematical foundations of common loss functions.
- Implement different
