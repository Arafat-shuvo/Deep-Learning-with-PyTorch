
# 08. Neural Network Architectures

## Overview

Neural Network Architectures define how neurons, layers, and computational operations are organized to learn patterns from data.

Different architectures are designed to solve different types of problems, including classification, regression, image recognition, sequence modeling, feature extraction, and natural language processing.

In this chapter, we will explore fundamental and advanced Neural Network architectures using PyTorch. We will start with the Perceptron and Multilayer Perceptron (MLP), then move toward CNNs, RNNs, LSTMs, GRUs, Autoencoders, and Transformer fundamentals.

The goal is to understand **how different Neural Network architectures work, their mathematical foundations, their implementations in PyTorch, and the types of problems they are designed to solve.**

## Learning Objectives

By completing this chapter, you will be able to:

- Understand the fundamental concepts of Neural Network architectures.
- Implement different architectures using PyTorch.
- Understand how neurons and layers are connected.
- Distinguish between shallow and deep Neural Networks.
- Understand architectures designed for image and sequential data.
- Implement CNN, RNN, LSTM, and GRU models.
- Understand the Encoder-Decoder structure of Autoencoders.
- Learn the fundamental concepts of Transformer architectures.
- Select suitable architectures for different deep learning tasks.

## Topics Covered

### 1. Perceptron

- Introduction to Perceptron.
- Biological Neuron vs Artificial Neuron.
- Structure of a Perceptron.
- Weights and Bias.
- Weighted Sum and Activation Function.
- Mathematical Foundation of Perceptron.
- Perceptron Learning Rule.
- Implementing a Perceptron using PyTorch.
- Understanding the Limitations of a Single-Layer Perceptron.

### 2. Multilayer Perceptron (MLP)

- Introduction to Multilayer Perceptron.
- Input Layer, Hidden Layers, and Output Layer.
- Understanding Neurons and Connections.
- Forward Propagation in MLP.
- Activation Functions in Hidden Layers.
- Mathematical Foundation of MLP.
- Implementing MLP using `nn.Module`.
- Training an MLP for Classification and Regression.

### 3. Artificial Neural Network (ANN)

- Introduction to Artificial Neural Networks.
- Understanding ANN Architecture.
- Fully Connected Layers.
- Input, Hidden, and Output Layers.
- Weights, Biases, and Activation Functions.
- Forward Propagation and Backpropagation.
- Implementing ANN using PyTorch.
- Building ANN Models for Classification and Regression.

### 4. Deep Neural Network (DNN)

- Introduction to Deep Neural Networks.
- Shallow Neural Networks vs Deep Neural Networks.
- Understanding Network Depth and Width.
- Multiple Hidden Layers.
- Representation Learning.
- Vanishing and Exploding Gradient Problems.
- Weight Initialization.
- Implementing Deep Neural Networks using PyTorch.
- Understanding Model Capacity and Overfitting.

### 5. Convolutional Neural Network (CNN)

- Introduction to Convolutional Neural Networks.
- Understanding Image Data and Tensor Dimensions.
- Convolution Operation.
- Filters and Kernels.
- Feature Maps.
- Stride and Padding.
- Pooling Operations.
- Max Pooling and Average Pooling.
- Flatten Layer.
- Fully Connected Layers in CNN.
- Implementing CNN using `nn.Conv2d()` and `nn.MaxPool2d()`.
- Building CNN Models for Image Classification.

### 6. Recurrent Neural Network (RNN)

- Introduction to Recurrent Neural Networks.
- Understanding Sequential Data.
- Recurrent Connections and Hidden States.
- Unrolling an RNN through Time.
- Forward Propagation in RNN.
- Mathematical Foundation of RNN.
- Backpropagation Through Time (BPTT).
- Vanishing and Exploding Gradients.
- Implementing RNN using `nn.RNN()`.
- Working with Sequential Input Data.

### 7. Long Short-Term Memory (LSTM)

- Introduction to Long Short-Term Memory.
- Why LSTM is needed.
- Understanding Cell State and Hidden State.
- Input Gate.
- Forget Gate.
- Output Gate.
- Candidate Cell State.
- Mathematical Foundation of LSTM.
- Implementing LSTM using `nn.LSTM()`.
- Understanding LSTM Input and Output Shapes.
- Building LSTM Models for Sequence Prediction.

### 8. Gated Recurrent Unit (GRU)

- Introduction to Gated Recurrent Unit.
- Understanding GRU Architecture.
- Update Gate.
- Reset Gate.
- Hidden State.
- Mathematical Foundation of GRU.
- Implementing GRU using `nn.GRU()`.
- Understanding GRU Input and Output Shapes.
- Comparing RNN, LSTM, and GRU.

### 9. Autoencoder

- Introduction to Autoencoders.
- Understanding Encoder and Decoder.
- Latent Space Representation.
- Bottleneck Layer.
- Reconstruction Loss.
- Training an Autoencoder.
- Implementing Autoencoder using PyTorch.
- Understanding Undercomplete and Overcomplete Autoencoders.
- Applications in Dimensionality Reduction and Anomaly Detection.

### 10. Transformer Fundamentals

- Introduction to Transformer Architecture.
- Understanding Sequence Modeling.
- Encoder and Decoder Architecture.
- Self-Attention Mechanism.
- Query, Key, and Value.
- Scaled Dot-Product Attention.
- Multi-Head Attention.
- Positional Encoding.
- Feed-Forward Neural Network.
- Residual Connections.
- Layer Normalization.
- Understanding Transformer Input and Output.
- Introduction to `nn.Transformer()`.

## Technologies & Libraries

- Python
- PyTorch
- NumPy
- Matplotlib
- Scikit-learn

## Folder Structure

```text
08. Neural Network Architectures/
│
├── README.md
│
├── 01_Perceptron/
│   └── perceptron.py
│
├── 02_Multilayer_Perceptron/
│   └── mlp.py
│
├── 03_Artificial_Neural_Network/
│   └── ann.py
│
├── 04_Deep_Neural_Network/
│   └── dnn.py
│
├── 05_Convolutional_Neural_Network/
│   ├── cnn.py
│   ├── convolution.py
│   └── pooling.py
│
├── 06_Recurrent_Neural_Network/
│   └── rnn.py
│
├── 07_Long_Short_Term_Memory/
│   └── lstm.py
│
├── 08_Gated_Recurrent_Unit/
│   └── gru.py
│
├── 09_Autoencoder/
│   └── autoencoder.py
│
└── 10_Transformer_Fundamentals/
    ├── self_attention.py
    ├── positional_encoding.py
    ├── multi_head_attention.py
    └── transformer.py
```

## Learning Approach

Each architecture will be implemented in a separate Python file.

For every architecture, we will:

1. Understand the theoretical concepts.
2. Study the architecture and its components.
3. Learn the mathematical foundations.
4. Understand the forward propagation process.
5. Implement the architecture using PyTorch.
6. Train the model using suitable datasets.
7. Evaluate its performance.
8. Analyze its strengths, limitations, and applications.

## Architecture Comparison

| Architecture | Primary Application |
|---|---|
| Perceptron | Basic binary classification |
| MLP | Classification and regression |
| ANN | General-purpose learning |
| DNN | Complex pattern learning |
| CNN | Image and spatial data |
| RNN | Sequential data |
| LSTM | Long-term sequence dependencies |
| GRU | Efficient sequence modeling |
| Autoencoder | Representation learning and reconstruction |
| Transformer | Attention-based sequence modeling |

## Expected Outcomes

After completing this chapter, you will be able to:

- Understand fundamental and advanced Neural Network architectures.
- Build different architectures using PyTorch.
- Explain the mathematical operations behind each architecture.
- Work with image, tabular, and sequential data.
- Understand the differences between CNN, RNN, LSTM, GRU, and Transformer.
- Build Encoder-Decoder architectures.
- Select suitable architectures for different deep learning problems.

## Next Chapter: Convolutional Neural Networks in Depth

After understanding the fundamental Neural Network architectures, we will explore CNNs in greater detail:

1. Convolution Mathematics
2. Different Convolution Operations
3. Padding and Stride
4. Pooling Operations
5. CNN Architecture Design
6. Batch Normalization
7. Dropout
8. Residual Connections
9. Advanced CNN Architectures
10. Transfer Learning

**Goal:** Develop a strong understanding of Neural Network architectures and build the foundation for advanced Deep Learning, Computer Vision, and Medical Image Analysis.
