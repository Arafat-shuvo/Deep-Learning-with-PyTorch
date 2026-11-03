# 06. Optimizers

## Overview

Optimizers are essential components of Neural Network training. They update the model's weights and biases using gradients calculated through backpropagation to minimize the loss function.

In this chapter, we will explore different optimization algorithms available in PyTorch, understand their mathematical foundations, and implement them using `torch.optim`.

We will also learn how Learning Rate, Weight Decay, and Learning Rate Scheduling affect the training process and model performance.

The goal is to understand **how different optimizers work, how they update model parameters, and how to select suitable optimization strategies for deep learning tasks.**

## Learning Objectives

By completing this chapter, you will be able to:

- Understand the role of optimizers in neural network training.
- Understand Gradient Descent and its mathematical foundation.
- Implement different optimization algorithms using PyTorch.
- Understand how momentum improves optimization.
- Identify the differences between SGD, Adagrad, RMSprop, Adam, and AdamW.
- Understand the importance of Learning Rate.
- Understand Weight Decay and its role in regularization.
- Implement Learning Rate Scheduling.
- Compare different optimizers based on convergence and performance.

## Topics Covered

### 1. Gradient Descent

- Introduction to Gradient Descent.
- Understanding gradients and parameter updates.
- Mathematical foundation of Gradient Descent.
- Understanding the optimization process.
- Implementing Gradient Descent using Python and PyTorch.
- Visualizing the optimization process.

### 2. Stochastic Gradient Descent (SGD)

- Introduction to Stochastic Gradient Descent.
- Batch Gradient Descent vs Stochastic Gradient Descent.
- Understanding Mini-Batch Gradient Descent.
- Mathematical foundation of SGD.
- Implementing `torch.optim.SGD()`.
- Understanding the advantages and limitations of SGD.

### 3. Momentum

- Introduction to Momentum.
- Why Momentum is needed.
- Understanding velocity and accumulated gradients.
- Mathematical foundation of Momentum.
- Implementing SGD with Momentum.
- Comparing SGD with and without Momentum.

### 4. Adagrad

- Introduction to Adaptive Gradient Algorithm.
- Understanding adaptive learning rates.
- Accumulation of squared gradients.
- Mathematical foundation of Adagrad.
- Implementing `torch.optim.Adagrad()`.
- Advantages and limitations of Adagrad.

### 5. RMSprop

- Introduction to RMSprop.
- Understanding exponentially weighted averages of squared gradients.
- How RMSprop adapts the learning rate.
- Mathematical foundation of RMSprop.
- Implementing `torch.optim.RMSprop()`.
- Comparing RMSprop with Adagrad.

### 6. Adam

- Introduction to Adaptive Moment Estimation.
- Understanding First Moment (Mean of Gradients).
- Understanding Second Moment (Uncentered Variance of Gradients).
- Bias Correction.
- Mathematical foundation of Adam.
- Implementing `torch.optim.Adam()`.
- Understanding Adam hyperparameters.

### 7. AdamW

- Introduction to AdamW.
- Understanding Weight Decay.
- Difference between Adam and AdamW.
- Decoupled Weight Decay.
- Mathematical foundation of AdamW.
- Implementing `torch.optim.AdamW()`.
- Understanding why AdamW is widely used in deep learning.

### 8. Learning Rate

- What is Learning Rate?
- Understanding the role of Learning Rate in optimization.
- Small vs Large Learning Rates.
- Learning Rate and Convergence.
- Learning Rate Selection.
- Understanding Learning Rate Sensitivity.
- Experimenting with different learning rates.

### 9. Weight Decay

- What is Weight Decay?
- Understanding L2 Regularization.
- How Weight Decay affects model parameters.
- Weight Decay and Overfitting.
- Difference between L2 Regularization and Decoupled Weight Decay.
- Implementing Weight Decay in PyTorch.

### 10. Learning Rate Scheduling

- Introduction to Learning Rate Scheduling.
- Why Learning Rate Scheduling is important.
- Understanding Learning Rate Decay.
- Implementing PyTorch Learning Rate Schedulers.
- StepLR.
- MultiStepLR.
- ExponentialLR.
- CosineAnnealingLR.
- ReduceLROnPlateau.
- Visualizing Learning Rate changes during training.

### 11. Optimizer Comparison

- Comparing SGD and Momentum.
- Comparing Adagrad and RMSprop.
- Comparing Adam and AdamW.
- Evaluating different optimizers with the same model and dataset.
- Comparing convergence speed and training loss.
- Analyzing the impact of Learning Rate and Weight Decay.
- Understanding optimizer selection for different tasks.

## Technologies & Libraries

- Python
- PyTorch
- NumPy
- Matplotlib

## Folder Structure

```text
06. Optimizers/
│
├── README.md
│
├── 01_Gradient_Descent/
│   └── gradient_descent.py
│
├── 02_Stochastic_Gradient_Descent/
│   └── sgd.py
│
├── 03_Momentum/
│   └── momentum.py
│
├── 04_Adagrad/
│   └── adagrad.py
│
├── 05_RMSprop/
│   └── rmsprop.py
│
├── 06_Adam/
│   └── adam.py
│
├── 07_AdamW/
│   └── adamw.py
│
├── 08_Learning_Rate/
│   └── learning_rate.py
│
├── 09_Weight_Decay/
│   └── weight_decay.py
│
├── 10_Learning_Rate_Scheduling/
│   ├── step_lr.py
│   ├── multi_step_lr.py
│   ├── exponential_lr.py
│   ├── cosine_annealing_lr.py
│   └── reduce_lr_on_plateau.py
│
└── 11_Optimizer_Comparison/
    └── optimizer_comparison.py
```

## Learning Approach

Each topic will be implemented in a separate Python file.

For every optimizer, we will:

1. Understand the mathematical concept.
2. Learn the mathematical equations.
3. Understand how gradients update model parameters.
4. Implement the algorithm using Python and PyTorch.
5. Train a simple neural network.
6. Monitor training loss and convergence.
7. Compare the optimizer's performance with other algorithms.

For optimizer comparison, we will try to keep the model architecture, dataset, and experimental conditions consistent to make the results meaningful.

## Expected Outcomes

After completing this chapter, you will be able to:

- Understand the mathematical foundations of optimization algorithms.
- Implement major optimizers in PyTorch.
- Explain how different optimizers update model parameters.
- Understand the impact of Learning Rate and Weight Decay.
- Apply Learning Rate Scheduling during training.
- Compare optimizer performance through experiments.
- Select appropriate optimizers for different deep learning tasks.

## Next Chapter: Neural Network Training

After understanding Optimizers, we will move to the next chapter:

1. Dataset Preparation
2. Training and Testing Data
3. DataLoader and Batch Processing
4. Forward Propagation
5. Loss Calculation
6. Backpropagation
7. Optimizer Step
8. Zero Gradients
9. Complete Training Loop
10. Model Evaluation and Validation

**Goal:** Combine Tensors, Autograd, Neural Network Layers, Loss Functions, and Optimizers to build and train a complete neural network using PyTorch.
