
# ============================================================
# Introduction to PyTorch
# Topic 02: PyTorch Fundamentals
# Author: Md. Arafat Hossain
#
# Topics Covered:
# 1. What is PyTorch?
# 2. Why PyTorch for Deep Learning?
# 3. PyTorch Features and Applications
# 4. PyTorch Installation and Setup
# 5. Understanding PyTorch Workflow
# ============================================================


# ============================================================
# 1. WHAT IS PYTORCH?
# ============================================================

# PyTorch is an open-source Deep Learning framework.
# It is developed and maintained by the PyTorch community
# with support from the PyTorch Foundation.
#
# PyTorch is mainly used for:
# - Machine Learning
# - Deep Learning
# - Neural Networks
# - Computer Vision
# - Natural Language Processing
#
# PyTorch provides tensors, automatic differentiation,
# neural network layers, optimizers, and GPU acceleration.

import torch

# Display PyTorch version
print("PyTorch Version:", torch.__version__)

# Create a simple tensor
x = torch.tensor([10, 20, 30, 40, 50])

print("Tensor:", x)


# ============================================================
# 2. WHY PYTORCH FOR DEEP LEARNING?
# ============================================================

# PyTorch is widely used in Deep Learning because it provides:
#
# 1. Easy-to-use Python interface
# 2. Automatic differentiation
# 3. GPU acceleration
# 4. Dynamic computation graphs
# 5. Flexible neural network development
# 6. Research-friendly environment
#
# Let's explore some important capabilities.


# ------------------------------------------------------------
# 2.1 Automatic Differentiation
# ------------------------------------------------------------

# Autograd automatically calculates gradients.
# Gradients are required to train neural networks.
#
# requires_grad=True tells PyTorch to track operations
# performed on this tensor.

a = torch.tensor(5.0, requires_grad=True)

# Mathematical operation
b = a ** 2

# Calculate gradients using backward()
b.backward()

# Display the gradient
print("\nAutomatic Differentiation:")
print("Value of a:", a.item())
print("Value of b:", b.item())
print("Gradient of a:", a.grad.item())

# Mathematical explanation:
# b = a^2
# db/da = 2a
# When a = 5, gradient = 10


# ------------------------------------------------------------
# 2.2 GPU Acceleration
# ------------------------------------------------------------

# PyTorch supports GPU computation using CUDA
# on compatible NVIDIA GPUs.
#
# torch.cuda.is_available() checks whether CUDA is available.

print("\nGPU Information:")

if torch.cuda.is_available():

    # Select CUDA device
    device = torch.device("cuda")

    print("CUDA Available: True")
    print("GPU Name:", torch.cuda.get_device_name(0))

else:

    # Use CPU if CUDA is unavailable
    device = torch.device("cpu")

    print("CUDA Available: False")
    print("Using CPU")

# Create a tensor on the selected device
gpu_tensor = torch.tensor([1, 2, 3], device=device)

print("Tensor Device:", gpu_tensor.device)


# ------------------------------------------------------------
# 2.3 Dynamic Computation Graph
# ------------------------------------------------------------

# PyTorch builds its computation graph dynamically
# while operations are executed.
#
# This makes it easier to build flexible neural networks.

x = torch.tensor(3.0, requires_grad=True)

y = x * 2
z = y + 5

print("\nDynamic Computation Graph:")
print("x:", x.item())
print("y:", y.item())
print("z:", z.item())

z.backward()

print("Gradient:", x.grad.item())


# ============================================================
# 3. PYTORCH FEATURES AND APPLICATIONS
# ============================================================

# Important PyTorch Features:
#
# 1. Tensor Computation
# 2. Automatic Differentiation (Autograd)
# 3. Neural Network Module (torch.nn)
# 4. Optimization Algorithms (torch.optim)
# 5. GPU Support (CUDA)
# 6. Dataset and DataLoader
# 7. Model Saving and Loading
# 8. Distributed Training


# ------------------------------------------------------------
# 3.1 Tensor Computation
# ------------------------------------------------------------

# Tensors are the fundamental data structures in PyTorch.
# They are similar to NumPy arrays but also support GPU computation.

tensor_a = torch.tensor([1, 2, 3])
tensor_b = torch.tensor([4, 5, 6])

print("\nTensor Computation:")

print("Addition:", tensor_a + tensor_b)
print("Subtraction:", tensor_a - tensor_b)
print("Multiplication:", tensor_a * tensor_b)


# ------------------------------------------------------------
# 3.2 Neural Network Module
# ------------------------------------------------------------

# torch.nn provides building blocks for neural networks.
# nn.Linear represents a fully connected linear layer.

import torch.nn as nn

# Create a linear layer:
# Input features = 3
# Output features = 2

linear_layer = nn.Linear(in_features=3, out_features=2)

# Input tensor with 3 features
input_data = torch.tensor([[1.0, 2.0, 3.0]])

# Forward propagation
output_data = linear_layer(input_data)

print("\nNeural Network Layer:")
print("Input:", input_data)
print("Output:", output_data)


# ------------------------------------------------------------
# 3.3 Optimization Algorithms
# ------------------------------------------------------------

# torch.optim provides optimization algorithms.
# These algorithms update model parameters during training.

optimizer = torch.optim.Adam(
    linear_layer.parameters(),
    lr=0.001
)

print("\nOptimizer:", optimizer)


# ------------------------------------------------------------
# 3.4 Dataset and DataLoader
# ------------------------------------------------------------

# Dataset stores samples and their corresponding labels.
# DataLoader helps load data in batches.

from torch.utils.data import TensorDataset, DataLoader

# Sample features
features = torch.tensor([
    [1.0, 2.0],
    [3.0, 4.0],
    [5.0, 6.0],
    [7.0, 8.0]
])

# Sample labels
labels = torch.tensor([0, 1, 0, 1])

# Create Dataset
dataset = TensorDataset(features, labels)

# Create DataLoader
dataloader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

print("\nDataLoader:")

for batch_features, batch_labels in dataloader:

    print("Features:", batch_features)
    print("Labels:", batch_labels)


# ------------------------------------------------------------
# 3.5 Applications of PyTorch
# ------------------------------------------------------------

# PyTorch is used in many Deep Learning applications.
#
# 1. Computer Vision
#    - Image Classification
#    - Object Detection
#    - Image Segmentation
#
# 2. Medical Image Analysis
#    - Brain Tumor Detection
#    - Brain Tumor Segmentation
#    - Medical Image Classification
#
# 3. Natural Language Processing
#    - Text Classification
#    - Machine Translation
#    - Language Models
#
# 4. Generative AI
#    - Image Generation
#    - Text Generation
#    - Diffusion Models
#
# 5. Time Series Forecasting
#    - Stock Prediction
#    - Weather Forecasting
#
# 6. Reinforcement Learning
#    - Game AI
#    - Robotics


# ============================================================
# 4. PYTORCH INSTALLATION AND SETUP
# ============================================================

# Step 1: Create a virtual environment.
#
# Command:
# python -m venv pytorch_env
#
# Step 2: Activate the virtual environment.
#
# Windows:
# pytorch_env\Scripts\activate
#
# Linux / macOS:
# source pytorch_env/bin/activate
#
# Step 3: Install PyTorch.
#
# Basic installation:
# pip install torch torchvision torchaudio
#
# For NVIDIA GPU/CUDA, choose the appropriate installation
# command from the official PyTorch website:
# https://pytorch.org/get-started/locally/
#
# Step 4: Verify the installation.


print("\nInstallation Verification:")

print("PyTorch Version:", torch.__version__)

print("CUDA Available:", torch.cuda.is_available())

if torch.cuda.is_available():

    print("CUDA Version:", torch.version.cuda)

    print("GPU Name:", torch.cuda.get_device_name(0))

else:

    print("Running on CPU")


# ============================================================
# 5. UNDERSTANDING PYTORCH WORKFLOW
# ============================================================

# A typical Deep Learning workflow consists of:
#
# 1. Data Preparation
# 2. Tensor Creation
# 3. Model Building
# 4. Forward Propagation
# 5. Loss Calculation
# 6. Backpropagation
# 7. Optimization
# 8. Model Evaluation
# 9. Model Saving


# ------------------------------------------------------------
# Step 1: Prepare Training Data
# ------------------------------------------------------------

# Create input features
X = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

# Create target values
# Our example relationship is approximately y = 2x + 1

Y = torch.tensor([
    [3.0],
    [5.0],
    [7.0],
    [9.0],
    [11.0]
])


# ------------------------------------------------------------
# Step 2: Build a Neural Network Model
# ------------------------------------------------------------

# nn.Module is the base class for PyTorch neural networks.

class SimpleModel(nn.Module):

    def __init__(self):

        super().__init__()

        # One input feature and one output feature
        self.linear = nn.Linear(1, 1)

    def forward(self, x):

        # Define forward propagation
        return self.linear(x)


# Create the model
model = SimpleModel()


# ------------------------------------------------------------
# Step 3: Define Loss Function
# ------------------------------------------------------------

# Mean Squared Error (MSE) measures the difference
# between predicted values and actual target values.

loss_function = nn.MSELoss()


# ------------------------------------------------------------
# Step 4: Define Optimizer
# ------------------------------------------------------------

# SGD updates model weights using calculated gradients.
# Learning rate controls the size of parameter updates.

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)


# ------------------------------------------------------------
# Step 5: Train the Model
# ------------------------------------------------------------

epochs = 1000

for epoch in range(epochs):

    # Forward Propagation
    predictions = model(X)

    # Calculate Loss
    loss = loss_function(predictions, Y)

    # Clear previous gradients
    optimizer.zero_grad()

    # Backpropagation
    loss.backward()

    # Update model parameters
    optimizer.step()

    # Display training progress
    if (epoch + 1) % 100 == 0:

        print(
            f"Epoch [{epoch + 1}/{epochs}], "
            f"Loss: {loss.item():.6f}"
        )


# ------------------------------------------------------------
# Step 6: Evaluate the Model
# ------------------------------------------------------------

# model.eval() switches the model to evaluation mode.
# torch.no_grad() disables gradient calculation.

model.eval()

with torch.no_grad():

    test_input = torch.tensor([[6.0]])

    prediction = model(test_input)

    print("\nModel Evaluation:")

    print("Input:", test_input.item())

    print("Predicted Output:", prediction.item())

    print("Expected Output:", 13.0)


# ------------------------------------------------------------
# Step 7: Save the Trained Model
# ------------------------------------------------------------

# state_dict() contains the model's learnable parameters.

torch.save(
    model.state_dict(),
    "simple_model.pth"
)

print("\nModel saved successfully!")


# ------------------------------------------------------------
# Step 8: Load the Trained Model
# ------------------------------------------------------------

# Create a new model instance
loaded_model = SimpleModel()

# Load saved parameters
loaded_model.load_state_dict(
    torch.load("simple_model.pth", map_location="cpu", weights_only=True)
)

# Set evaluation mode
loaded_model.eval()

# Test loaded model
with torch.no_grad():

    loaded_prediction = loaded_model(
        torch.tensor([[6.0]])
    )

print("Loaded Model Prediction:", loaded_prediction.item())


# ============================================================
# END OF INTRODUCTION TO PYTORCH
# ============================================================

# What We Learned:
#
# 1. What PyTorch is
# 2. Why PyTorch is useful for Deep Learning
# 3. Important PyTorch features
# 4. Applications of PyTorch
# 5. PyTorch installation and setup
# 6. Tensor computation
# 7. Automatic differentiation
# 8. GPU acceleration
# 9. Neural network construction
# 10. Complete Deep Learning training workflow
#
# NEXT TOPIC:
# Introduction to PyTorch Tensors
#
# We will learn:
# - What is a Tensor?
# - Creating Tensors
# - Tensor Dimensions
# - Tensor Attributes
# - Tensor Data Types
# - Tensor Operations
# ============================================================
