# 04. Neural Network Fundamentals

Welcome to **Neural Network Fundamentals**, the fourth chapter of my journey toward mastering Deep Learning with PyTorch.

This chapter focuses on understanding the fundamental building blocks of Neural Networks, including Object-Oriented Programming (OOP), PyTorch's `nn.Module`, Linear Layers, Weights, Biases, Matrix Multiplication, and Activation Functions.

The primary goal is to understand how individual neurons and layers work mathematically and how they are implemented using PyTorch before moving into complete Neural Network architectures and model training.

## 🎯 Learning Objectives

- Understand Python Classes and Objects.
- Learn the structure and functionality of `nn.Module`.
- Understand `__init__()`, `super().__init__()`, and `forward()`.
- Create custom Neural Network layers using PyTorch.
- Understand `nn.Linear()` and its internal operations.
- Understand Weights and Bias mathematically.
- Learn how Matrix Multiplication works inside Linear Layers.
- Understand the importance of Activation Functions.
- Implement different Activation Functions using PyTorch.
- Build a foundation for designing custom Neural Network architectures.

## 📚 Topics Covered

### 1. Class and Object

- Introduction to Object-Oriented Programming (OOP)
- What is a Class?
- What is an Object?
- Attributes and Methods
- Constructors
- Instance Variables
- Creating Classes and Objects in Python
- Understanding OOP in PyTorch

### 2. `nn.Module`

- What is `nn.Module`?
- Why Do We Need `nn.Module`?
- Understanding PyTorch Neural Network Modules
- Creating Custom Neural Network Classes
- Inheriting from `nn.Module`
- Registering Parameters and Layers
- `parameters()` and `named_parameters()`
- `state_dict()`
- Understanding Model Structure

### 3. `__init__()`

- What is `__init__()`?
- Constructor in Python
- Initializing Neural Network Layers
- Defining Model Parameters
- Creating Layers Inside `__init__()`
- Understanding Initialization Workflow

### 4. `super().__init__()`

- What is `super()`?
- Understanding Parent and Child Classes
- Why Use `super().__init__()`?
- Inheritance in PyTorch
- Initializing the Parent `nn.Module`
- What Happens Without `super().__init__()`?
- Practical Implementation

### 5. `forward()`

- What is `forward()`?
- Understanding Forward Propagation
- Defining Forward Computation
- Passing Input Through Layers
- Returning Model Outputs
- Layer-by-Layer Computation
- How PyTorch Calls `forward()`
- Understanding `model(x)` vs `model.forward(x)`

### 6. `nn.Linear`

- What is `nn.Linear()`?
- Understanding Linear Layers
- `in_features`
- `out_features`
- Creating Linear Layers
- Input and Output Tensor Shapes
- Multiple Linear Layers
- Stacking Linear Layers
- Practical Implementation

### 7. Weights and Bias

- What are Weights?
- What is Bias?
- Understanding Trainable Parameters
- Weight Initialization
- Bias Initialization
- Accessing Weights and Bias
- `layer.weight`
- `layer.bias`
- How Weights and Bias Affect Output
- Learnable Parameters in Neural Networks

### 8. Matrix Multiplication in Linear Layers

- Mathematical Foundation of Linear Transformation
- Understanding Input Matrix
- Weight Matrix
- Bias Vector
- Matrix Dimensions and Shapes
- Matrix Multiplication
- Broadcasting Bias
- Understanding Linear Layer Computation
- Manual Linear Layer Implementation
- Comparing Manual Computation with `nn.Linear()`

### 9. Activation Functions

- What are Activation Functions?
- Why Do Neural Networks Need Activation Functions?
- Linear vs Non-linear Transformations
- Activation Functions and Decision Boundaries
- Implementing Activation Functions in PyTorch

#### 9.1 ReLU (Rectified Linear Unit)

- Introduction to ReLU
- Mathematical Definition
- Forward Computation
- Advantages and Limitations
- `nn.ReLU()`
- `torch.relu()`

#### 9.2 Leaky ReLU

- Introduction to Leaky ReLU
- Dying ReLU Problem
- Negative Slope
- Mathematical Definition
- `nn.LeakyReLU()`
- ReLU vs Leaky ReLU

#### 9.3 Sigmoid

- Introduction to Sigmoid
- Mathematical Definition
- Output Range (0 to 1)
- Sigmoid Curve
- Gradient and Saturation
- `nn.Sigmoid()`
- Applications in Binary Classification

#### 9.4 Tanh

- Introduction to Tanh
- Mathematical Definition
- Output Range (-1 to 1)
- Tanh Curve
- Zero-Centered Activation
- `nn.Tanh()`
- Sigmoid vs Tanh

#### 9.5 Softmax

- Introduction to Softmax
- Mathematical Definition
- Converting Logits into Probabilities
- Probability Distribution
- Understanding Output Dimensions
- `nn.Softmax()`
- Applications in Multiclass Classification
- Softmax vs Sigmoid

## 🛠️ Technologies & Libraries

- Python
- PyTorch
- NumPy
- Matplotlib
- Jupyter Notebook
- VS Code

## 📂 Folder Structure

```text
04. Neural Network Fundamentals/
│
├── 01. Class and Object/
│   ├── class_basics.py
│   ├── object_basics.py
│   └── oop_in_pytorch.py
│
├── 02. nn.Module/
│   ├── nn_module_basics.py
│   ├── custom_module.py
│   └── model_parameters.py
│
├── 03. __init__()/
│   ├── constructor_basics.py
│   └── initialize_layers.py
│
├── 04. super().__init__()/
│   ├── inheritance.py
│   └── super_init.py
│
├── 05. forward()/
│   ├── forward_basics.py
│   ├── forward_propagation.py
│   └── model_execution.py
│
├── 06. nn.Linear/
│   ├── linear_basics.py
│   ├── input_output_features.py
│   └── multiple_linear_layers.py
│
├── 07. Weights and Bias/
│   ├── weights.py
│   ├── bias.py
│   └── parameter_initialization.py
│
├── 08. Matrix Multiplication in Linear Layers/
│   ├── linear_mathematics.py
│   ├── manual_linear_layer.py
│   └── pytorch_linear_comparison.py
│
└── 09. Activation Functions/
    │
    ├── 01. ReLU/
    │   ├── relu_basics.py
    │   └── relu_visualization.py
    │
    ├── 02. Leaky ReLU/
    │   ├── leaky_relu.py
    │   └── relu_vs_leaky_relu.py
    │
    ├── 03. Sigmoid/
    │   ├── sigmoid_basics.py
    │   └── sigmoid_visualization.py
    │
    ├── 04. Tanh/
    │   ├── tanh_basics.py
    │   └── tanh_visualization.py
    │
    └── 05. Softmax/
        ├── softmax_basics.py
        └── softmax_probabilities.py
```

## 🚀 Learning Approach

Each topic will be implemented in a separate Python file.

1. Understand the theoretical concepts.
2. Learn the mathematical foundations.
3. Understand Python OOP concepts.
4. Implement custom classes using `nn.Module`.
5. Explore the internal operations of `nn.Linear()`.
6. Calculate Linear Layer outputs manually.
7. Implement Activation Functions using PyTorch.
8. Visualize activation functions using Matplotlib.
9. Compare different Activation Functions.
10. Build simple Neural Network components from scratch.

## 🎓 Expected Outcome

After completing this chapter, I will be able to:

- Understand Object-Oriented Programming in Python.
- Create custom Neural Network models using `nn.Module`.
- Understand the roles of `__init__()`, `super().__init__()`, and `forward()`.
- Create and configure Linear Layers using `nn.Linear()`.
- Understand Weights, Bias, and trainable parameters.
- Perform Linear Transformations using Matrix Multiplication.
- Understand and implement ReLU, Leaky ReLU, Sigmoid, Tanh, and Softmax.
- Build the fundamental components of a Neural Network using PyTorch.

## 📖 Next Chapter: Neural Network Training

After completing Neural Network Fundamentals, the next chapter will cover:

- Loss Functions
- Mean Squared Error (MSE)
- Binary Cross Entropy (BCE)
- Cross Entropy Loss
- Optimizers
- Stochastic Gradient Descent (SGD)
- Adam and AdamW
- Learning Rate
- Training Loop
- Model Evaluation

**Goal:** Understand how Neural Network layers, weights, biases, and activation functions work internally before learning how to train complete Neural Networks.

---

**Learning Path:** Python & NumPy → PyTorch Fundamentals → Autograd → Neural Network Fundamentals → Neural Network Training → Deep Learning.
