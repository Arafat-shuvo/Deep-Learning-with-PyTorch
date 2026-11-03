# 02. PyTorch Fundamentals

Welcome to **PyTorch Fundamentals**, the second chapter of my journey toward mastering Deep Learning with PyTorch.

This chapter focuses on understanding PyTorch, tensors, tensor manipulation, mathematical operations, matrix computations, and GPU acceleration.

The primary goal is to develop a strong understanding of PyTorch's fundamental data structures and operations before moving into Autograd, Neural Networks, and Deep Learning architectures.

## 🎯 Learning Objectives

- Understand PyTorch and its role in Deep Learning.
- Compare PyTorch with TensorFlow.
- Understand tensors and their properties.
- Learn scalar, vector, matrix, and multidimensional tensors.
- Create and manipulate PyTorch tensors.
- Perform mathematical and matrix operations.
- Understand tensor reshaping and broadcasting.
- Execute tensor operations on CPU and GPU.
- Understand CUDA fundamentals and GPU acceleration.

## 📚 Topics Covered

### 1. Introduction to PyTorch

- What is PyTorch?
- Why PyTorch for Deep Learning?
- PyTorch Features and Applications
- PyTorch Installation and Setup
- Understanding PyTorch Workflow

### 2. PyTorch vs TensorFlow

- Introduction to TensorFlow
- PyTorch vs TensorFlow
- Dynamic vs Static Computational Graphs
- Eager Execution
- Advantages and Disadvantages
- Choosing the Right Framework

### 3. Tensors and Their Properties

- What is a Tensor?
- Tensor Properties
- Data Types (`dtype`)
- Device (`device`)
- Shape and Dimensions
- Memory and Storage Basics

### 4. Scalar, Vector and Matrix

- Understanding Scalars
- Understanding Vectors
- Understanding Matrices
- Multidimensional Tensors
- Practical Tensor Examples

### 5. Tensor Dimensions and Shapes

- Tensor Dimensions (`ndim`)
- Tensor Shape (`shape`)
- Tensor Size (`size()`)
- Understanding Axes
- Dimension Manipulation

### 6. Tensor Creation

- `torch.tensor()`
- `torch.zeros()`
- `torch.ones()`
- `torch.empty()`
- `torch.arange()`
- `torch.linspace()`
- `torch.rand()`
- `torch.randn()`
- `torch.eye()`
- Setting Data Types and Devices

### 7. Tensor Indexing and Slicing

- Basic Tensor Indexing
- Multi-dimensional Indexing
- Tensor Slicing
- Selecting Specific Elements
- Advanced Indexing
- Boolean Masking

### 8. Reshape, View and Flatten

- `reshape()`
- `view()`
- `flatten()`
- Understanding Contiguous Tensors
- Difference Between `reshape()` and `view()`
- Practical Shape Manipulation

### 9. Squeeze and Unsqueeze

- `squeeze()`
- `unsqueeze()`
- Removing Singleton Dimensions
- Adding New Dimensions
- Understanding Dimension Changes

### 10. Tensor Operations

- Arithmetic Operations
- Element-wise Operations
- Addition and Subtraction
- Multiplication and Division
- Comparison Operations
- Aggregation Operations
- Sum, Mean, Max and Min
- In-place Operations

### 11. Matrix Multiplication

- Matrix Multiplication Fundamentals
- `torch.matmul()`
- `torch.mm()`
- `torch.mv()`
- `torch.dot()`
- `@` Operator
- Understanding Matrix Shapes
- Practical Matrix Multiplication

### 12. Broadcasting

- Introduction to Broadcasting
- Broadcasting Rules
- Broadcasting with Scalars
- Broadcasting with Vectors
- Broadcasting with Matrices
- Practical Broadcasting Examples

### 13. CPU and GPU Operations

- Understanding CPU and GPU
- Checking Available Devices
- Creating CPU Tensors
- Creating GPU Tensors
- Moving Tensors Between Devices
- `.to()` and `.cuda()`
- Device Compatibility
- GPU Acceleration

### 14. CUDA Fundamentals

- What is CUDA?
- Introduction to NVIDIA CUDA
- CUDA and PyTorch
- Checking CUDA Availability
- `torch.cuda.is_available()`
- `torch.cuda.get_device_name()`
- GPU Memory Management
- CPU vs GPU Performance Comparison

## 🛠️ Technologies & Libraries

- Python
- PyTorch
- NumPy
- CUDA
- NVIDIA GPU
- Jupyter Notebook
- VS Code

## 📂 Folder Structure

```text
02. PyTorch Fundamentals/
│
├── 01. Introduction to PyTorch/
│   ├── pytorch_introduction.py
│   ├── pytorch_features.py
│   └── pytorch_vs_tensorflow.py
│
├── 02. Tensors and Their Properties/
│   ├── tensor_basics.py
│   ├── tensor_properties.py
│   └── tensor_dtype_device.py
│
├── 03. Scalar, Vector and Matrix/
│   ├── scalar.py
│   ├── vector.py
│   ├── matrix.py
│   └── multidimensional_tensor.py
│
├── 04. Tensor Dimensions and Shapes/
│   ├── tensor_dimensions.py
│   ├── tensor_shapes.py
│   └── tensor_axes.py
│
├── 05. Tensor Creation/
│   ├── tensor_creation.py
│   ├── zeros_ones.py
│   ├── random_tensors.py
│   └── identity_tensor.py
│
├── 06. Tensor Indexing and Slicing/
│   ├── indexing.py
│   ├── slicing.py
│   └── boolean_masking.py
│
├── 07. Reshape, View and Flatten/
│   ├── reshape.py
│   ├── view.py
│   └── flatten.py
│
├── 08. Squeeze and Unsqueeze/
│   ├── squeeze.py
│   └── unsqueeze.py
│
├── 09. Tensor Operations/
│   ├── arithmetic_operations.py
│   ├── elementwise_operations.py
│   └── aggregation.py
│
├── 10. Matrix Multiplication/
│   ├── matrix_multiplication.py
│   ├── torch_matmul.py
│   └── dot_product.py
│
├── 11. Broadcasting/
│   ├── broadcasting_basics.py
│   └── broadcasting_examples.py
│
├── 12. CPU and GPU Operations/
│   ├── cpu_operations.py
│   ├── gpu_operations.py
│   └── device_transfer.py
│
└── 13. CUDA Fundamentals/
    ├── cuda_availability.py
    ├── cuda_device_info.py
    └── cpu_vs_gpu.py
```

## 🚀 Learning Approach

Each topic will be implemented in a separate Python file.

1. Understand the theoretical concepts.
2. Learn the mathematical foundations.
3. Understand tensor shapes and dimensions.
4. Implement operations using PyTorch.
5. Compare results with NumPy where appropriate.
6. Practice with different examples.
7. Run experiments on CPU and GPU.

## 🎓 Expected Outcome

After completing this chapter, I will be able to:

- Understand PyTorch fundamentals.
- Create and manipulate tensors of different dimensions.
- Perform mathematical and matrix operations.
- Understand tensor shapes, dimensions, and broadcasting.
- Work with CPU and GPU devices.
- Understand CUDA and GPU acceleration.
- Prepare for PyTorch Autograd and Neural Network development.

## 📖 Next Chapter: PyTorch Autograd

After completing PyTorch Fundamentals, the next chapter will cover:

- Derivatives and Gradients
- Computational Graph
- `requires_grad=True`
- `backward()`
- Chain Rule
- Automatic Differentiation
- Backpropagation Fundamentals

**Goal:** Understand how PyTorch handles tensors and mathematical computations internally before learning automatic differentiation and neural network training.

---

**Learning Path:** Python & NumPy → PyTorch Fundamentals → Autograd → Neural Networks → Deep Learning.
