# 03. PyTorch Autograd

Welcome to **PyTorch Autograd**, the third chapter of my journey toward mastering Deep Learning with PyTorch.

This chapter focuses on Automatic Differentiation, derivatives, gradients, computational graphs, and backpropagation mathematics.

The primary goal is to understand how PyTorch automatically calculates gradients and how these gradients are used to update neural network parameters during the training process.

## 🎯 Learning Objectives

- Understand derivatives and gradients mathematically.
- Learn the concept of Automatic Differentiation.
- Understand how PyTorch builds Computational Graphs.
- Learn how `requires_grad` tracks tensor operations.
- Understand how `backward()` calculates gradients.
- Perform manual and automatic gradient calculations.
- Understand gradient accumulation and zeroing gradients.
- Learn the Chain Rule and its application in Backpropagation.
- Understand how gradients flow through neural networks.
- Control gradient tracking using `torch.no_grad()` and `detach()`.

## 📚 Topics Covered

### 1. Derivatives and Gradients

- Introduction to Derivatives
- Understanding Differentiation
- Partial Derivatives
- Introduction to Gradients
- Gradient of a Scalar Function
- Gradient of Multivariable Functions
- Geometrical Interpretation of Gradients
- Practical Derivative Calculations

### 2. Computational Graph

- What is a Computational Graph?
- Nodes and Edges
- Forward Computation
- Graph Construction in PyTorch
- Understanding Dependencies
- Dynamic Computational Graph
- Computational Graph Visualization

### 3. `requires_grad`

- What is `requires_grad`?
- Setting `requires_grad=True`
- Tracking Tensor Operations
- Understanding Gradient Tracking
- `requires_grad` Property
- `is_leaf` Property
- `grad_fn` Attribute

### 4. `backward()`

- What is `backward()`?
- How `backward()` Works
- Automatic Gradient Calculation
- Calling `backward()` on Scalar Outputs
- Understanding the `gradient` Argument
- Accessing Gradients Using `.grad`
- Practical Examples

### 5. Gradient Calculation

- Understanding Gradient Calculation
- Manual Gradient Calculation
- Automatic Gradient Calculation
- Scalar Function Gradients
- Multivariable Function Gradients
- Vector and Matrix Gradients
- Comparing Manual and PyTorch Calculations

### 6. Gradient Accumulation

- What is Gradient Accumulation?
- How PyTorch Accumulates Gradients
- Understanding `.grad`
- Multiple `backward()` Calls
- Gradient Accumulation in Training
- Practical Gradient Accumulation Examples

### 7. Zero Gradients

- Why Gradients Must Be Reset
- Understanding `zero_grad()`
- `optimizer.zero_grad()`
- `tensor.grad.zero_()`
- `set_to_none=True`
- Gradient Resetting in Training Loops
- Common Gradient Management Mistakes

### 8. Chain Rule

- Introduction to the Chain Rule
- Mathematical Foundation
- Derivatives of Composite Functions
- Partial Derivatives and Chain Rule
- Chain Rule with Multiple Variables
- Computational Graph and Chain Rule
- Practical PyTorch Implementation

### 9. Backpropagation Mathematics

- What is Backpropagation?
- Forward Propagation
- Loss Function
- Computing Gradients
- Backward Propagation
- Weight and Bias Gradients
- Parameter Updates
- Backpropagation in a Single Neuron
- Backpropagation in a Multi-layer Neural Network
- Mathematical Implementation Using PyTorch

### 10. `torch.no_grad()`

- What is `torch.no_grad()`?
- Disabling Gradient Tracking
- Context Manager
- Inference Without Gradient Calculation
- Reducing Memory Consumption
- Training vs Inference
- Practical Examples

### 11. `detach()`

- What is `detach()`?
- Detaching a Tensor from Computational Graph
- Understanding Detached Tensors
- `detach()` vs `torch.no_grad()`
- Gradient Tracking After Detachment
- Detached Tensor Operations
- Practical Examples

## 🛠️ Technologies & Libraries

- Python
- PyTorch
- NumPy
- Matplotlib
- Jupyter Notebook
- VS Code

## 📂 Folder Structure

```text
03. Autograd/
│
├── 01. Derivatives and Gradients/
│   ├── derivatives.py
│   ├── partial_derivatives.py
│   └── gradients.py
│
├── 02. Computational Graph/
│   ├── computational_graph.py
│   ├── forward_computation.py
│   └── graph_visualization.py
│
├── 03. requires_grad/
│   ├── requires_grad_basics.py
│   ├── gradient_tracking.py
│   └── grad_fn_leaf_tensors.py
│
├── 04. backward()/
│   ├── backward_basics.py
│   ├── automatic_gradients.py
│   └── backward_examples.py
│
├── 05. Gradient Calculation/
│   ├── manual_gradient.py
│   ├── automatic_gradient.py
│   └── multivariable_gradients.py
│
├── 06. Gradient Accumulation/
│   ├── gradient_accumulation.py
│   └── multiple_backward.py
│
├── 07. Zero Gradients/
│   ├── zero_grad_basics.py
│   ├── optimizer_zero_grad.py
│   └── gradient_resetting.py
│
├── 08. Chain Rule/
│   ├── chain_rule_basics.py
│   ├── multivariable_chain_rule.py
│   └── chain_rule_pytorch.py
│
├── 09. Backpropagation Mathematics/
│   ├── forward_propagation.py
│   ├── loss_calculation.py
│   ├── backward_propagation.py
│   └── manual_backpropagation.py
│
├── 10. torch.no_grad()/
│   ├── no_grad_basics.py
│   └── inference_mode.py
│
└── 11. detach()/
    ├── detach_basics.py
    └── detach_vs_no_grad.py
```

## 🚀 Learning Approach

Each topic will be implemented in a separate Python file.

1. Understand the mathematical concepts.
2. Derive gradients manually using calculus.
3. Visualize computational graphs.
4. Implement gradient calculations using PyTorch.
5. Compare manual and automatic differentiation.
6. Experiment with multiple `backward()` calls.
7. Understand gradient accumulation and resetting.
8. Implement backpropagation step by step.
9. Practice controlling gradient tracking.

## 🎓 Expected Outcome

After completing this chapter, I will be able to:

- Understand derivatives, partial derivatives, and gradients.
- Explain how computational graphs work.
- Use PyTorch Autograd for automatic differentiation.
- Calculate gradients using `backward()`.
- Understand gradient accumulation and gradient resetting.
- Apply the Chain Rule mathematically.
- Explain the mathematics behind backpropagation.
- Control gradient tracking using `torch.no_grad()` and `detach()`.
- Understand how gradients are calculated during neural network training.

## 📖 Next Chapter: PyTorch Neural Networks

After completing Autograd, the next chapter will cover:

- `nn.Module`
- `nn.Linear`
- Weights and Bias
- Activation Functions
- Forward Propagation
- Loss Functions
- Optimizers
- Neural Network Training

**Goal:** Understand the mathematical foundation of Automatic Differentiation and Backpropagation before building and training Neural Networks using PyTorch.

---

**Learning Path:** Python & NumPy → PyTorch Fundamentals → Autograd → Neural Networks → Deep Learning.
