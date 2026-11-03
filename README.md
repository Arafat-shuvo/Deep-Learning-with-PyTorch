# PyTorch Learning Repository
### From Basic to Advanced | Theory, Mathematics & Hands-on Implementation

![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?logo=pytorch&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Learning](https://img.shields.io/badge/Learning-Basic%20to%20Advanced-blue)
![Status](https://img.shields.io/badge/Status-Learning%20in%20Progress-orange)

## About This Repository

This repository documents my journey of learning **PyTorch**, starting from fundamental concepts to advanced deep learning techniques.

The goal is not just to learn PyTorch syntax but to understand the underlying mathematics, implement neural networks from scratch, train deep learning models, and conduct practical experiments.

Each topic is organized into separate Python files for better understanding, practice, and reproducibility.

## Learning Roadmap

### 01. Python & NumPy Foundations

- [ ] Python Basics for Deep Learning
- [ ] NumPy Arrays
- [ ] Array Operations
- [ ] Broadcasting
- [ ] Matrix Operations
- [ ] Linear Algebra Fundamentals

### 02. PyTorch Fundamentals

- [ ] Introduction to PyTorch
- [ ] PyTorch vs TensorFlow
- [ ] Tensors and Their Properties
- [ ] Scalar, Vector and Matrix
- [ ] Tensor Dimensions and Shapes
- [ ] Tensor Creation
- [ ] Tensor Indexing and Slicing
- [ ] Reshape, View and Flatten
- [ ] Squeeze and Unsqueeze
- [ ] Tensor Operations
- [ ] Matrix Multiplication
- [ ] Broadcasting
- [ ] CPU and GPU Operations
- [ ] CUDA Fundamentals

### 03. Autograd

- [ ] Derivatives and Gradients
- [ ] Computational Graph
- [ ] requires_grad
- [ ] backward()
- [ ] Gradient Calculation
- [ ] Gradient Accumulation
- [ ] Zero Gradients
- [ ] Chain Rule
- [ ] Backpropagation Mathematics
- [ ] torch.no_grad()
- [ ] detach()

### 04. Neural Network Fundamentals

- [ ] Class and Object
- [ ] nn.Module
- [ ] __init__()
- [ ] super().__init__()
- [ ] forward()
- [ ] nn.Linear
- [ ] Weights and Bias
- [ ] Matrix Multiplication in Linear Layers
- [ ] Activation Functions
  - ReLU
  - Leaky ReLU
  - Sigmoid
  - Tanh
  - Softmax

### 05. Loss Functions

- [ ] Mean Squared Error (MSE)
- [ ] Mean Absolute Error (MAE)
- [ ] Binary Cross Entropy
- [ ] BCEWithLogitsLoss
- [ ] Cross Entropy Loss
- [ ] Loss Function Comparison

### 06. Optimizers

- [ ] Gradient Descent
- [ ] Stochastic Gradient Descent (SGD)
- [ ] Momentum
- [ ] Adagrad
- [ ] RMSprop
- [ ] Adam
- [ ] AdamW
- [ ] Learning Rate
- [ ] Weight Decay
- [ ] Learning Rate Scheduling

### 07. Training Neural Networks

- [ ] Dataset Preparation
- [ ] DataLoader
- [ ] TensorDataset
- [ ] Custom Dataset
- [ ] Forward Propagation
- [ ] Loss Calculation
- [ ] Backward Propagation
- [ ] Optimizer Step
- [ ] Complete Training Loop
- [ ] Validation Loop
- [ ] Model Evaluation
- [ ] Model Saving and Loading

### 08. Neural Network Architectures

- [ ] Perceptron
- [ ] Multilayer Perceptron (MLP)
- [ ] Artificial Neural Network (ANN)
- [ ] Deep Neural Network (DNN)
- [ ] Convolutional Neural Network (CNN)
- [ ] Recurrent Neural Network (RNN)
- [ ] Long Short-Term Memory (LSTM)
- [ ] Gated Recurrent Unit (GRU)
- [ ] Autoencoder
- [ ] Transformer Fundamentals

### 09. Computer Vision with PyTorch

- [ ] Image Loading and Preprocessing
- [ ] torchvision
- [ ] Image Classification
- [ ] CNN Architecture
- [ ] Transfer Learning
- [ ] ResNet
- [ ] DenseNet
- [ ] EfficientNet
- [ ] U-Net
- [ ] U-Net++
- [ ] Object Detection
- [ ] Semantic Segmentation
- [ ] Medical Image Segmentation

### 10. Advanced PyTorch

- [ ] Custom Neural Network Layers
- [ ] Custom Loss Functions
- [ ] Custom Optimizers
- [ ] Weight Initialization
- [ ] Batch Normalization
- [ ] Layer Normalization
- [ ] Dropout
- [ ] Attention Mechanism
- [ ] Transformer Architecture
- [ ] Mixed Precision Training
- [ ] Gradient Clipping
- [ ] Transfer Learning
- [ ] Model Checkpointing
- [ ] Reproducibility and Random Seeds
- [ ] Hyperparameter Optimization
- [ ] Model Deployment
- [ ] PyTorch Profiler

---

## Repository Structure

Each topic will have its own Python file, organized into separate folders.

```text
pytorch-learning/
│
├── README.md
├── requirements.txt
│
├── 01_python_numpy/
│   ├── 01_python_basics.py
│   ├── 02_numpy_arrays.py
│   ├── 03_array_operations.py
│   ├── 04_broadcasting.py
│   └── 05_matrix_operations.py
│
├── 02_pytorch_fundamentals/
│   ├── 01_tensor_creation.py
│   ├── 02_tensor_properties.py
│   ├── 03_scalar_vector_matrix.py
│   ├── 04_tensor_dimensions.py
│   ├── 05_tensor_indexing.py
│   ├── 06_reshape_view_flatten.py
│   ├── 07_squeeze_unsqueeze.py
│   ├── 08_tensor_operations.py
│   ├── 09_matrix_multiplication.py
│   ├── 10_broadcasting.py
│   └── 11_cuda_operations.py
│
├── 03_autograd/
│   ├── 01_derivatives.py
│   ├── 02_gradients.py
│   ├── 03_computational_graph.py
│   ├── 04_requires_grad.py
│   ├── 05_backward.py
│   ├── 06_gradient_accumulation.py
│   ├── 07_zero_grad.py
│   ├── 08_chain_rule.py
│   └── 09_backpropagation.py
│
├── 04_neural_network/
│   ├── 01_class_object.py
│   ├── 02_nn_module.py
│   ├── 03_init_super.py
│   ├── 04_forward_method.py
│   ├── 05_nn_linear.py
│   ├── 06_weights_bias.py
│   └── 07_activation_functions.py
│
├── 05_loss_functions/
│   ├── 01_mse_loss.py
│   ├── 02_mae_loss.py
│   ├── 03_binary_cross_entropy.py
│   ├── 04_bce_with_logits.py
│   └── 05_cross_entropy.py
│
├── 06_optimizers/
│   ├── 01_gradient_descent.py
│   ├── 02_sgd.py
│   ├── 03_momentum.py
│   ├── 04_adagrad.py
│   ├── 05_rmsprop.py
│   ├── 06_adam.py
│   ├── 07_adamw.py
│   └── 08_lr_scheduler.py
│
├── 07_training/
│   ├── 01_tensor_dataset.py
│   ├── 02_dataloader.py
│   ├── 03_custom_dataset.py
│   ├── 04_forward_propagation.py
│   ├── 05_backward_propagation.py
│   ├── 06_training_loop.py
│   ├── 07_validation.py
│   ├── 08_evaluation.py
│   └── 09_save_load_model.py
│
├── 08_architectures/
│   ├── 01_perceptron.py
│   ├── 02_mlp.py
│   ├── 03_ann.py
│   ├── 04_dnn.py
│   ├── 05_cnn.py
│   ├── 06_rnn.py
│   ├── 07_lstm.py
│   ├── 08_gru.py
│   ├── 09_autoencoder.py
│   └── 10_transformer.py
│
├── 09_computer_vision/
│   ├── 01_image_loading.py
│   ├── 02_image_preprocessing.py
│   ├── 03_image_classification.py
│   ├── 04_transfer_learning.py
│   ├── 05_resnet.py
│   ├── 06_densenet.py
│   ├── 07_efficientnet.py
│   ├── 08_unet.py
│   ├── 09_unet_plus_plus.py
│   └── 10_image_segmentation.py
│
├── 10_advanced_pytorch/
│   ├── 01_custom_layer.py
│   ├── 02_custom_loss.py
│   ├── 03_custom_optimizer.py
│   ├── 04_weight_initialization.py
│   ├── 05_batch_normalization.py
│   ├── 06_dropout.py
│   ├── 07_attention.py
│   ├── 08_transformer.py
│   ├── 09_mixed_precision.py
│   ├── 10_gradient_clipping.py
│   ├── 11_checkpointing.py
│   ├── 12_reproducibility.py
│   └── 13_profiler.py
│
└── projects/
    ├── 01_linear_regression/
    ├── 02_binary_classification/
    ├── 03_mnist_classification/
    ├── 04_cnn_image_classification/
    ├── 05_lstm_prediction/
    ├── 06_custom_cnn/
    └── 07_brain_tumor_segmentation/
```

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/Arafat-shuvo/pytorch-learning.git
cd pytorch-learning
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the environment**

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run any topic**

```bash
python 02_pytorch_fundamentals/01_tensor_creation.py
```

## Learning Methodology

Every Python file will follow a consistent learning structure:

1. Concept — Understand the topic.
2. Mathematics — Understand the underlying equations.
3. Implementation — Write PyTorch code.
4. Experiment — Modify parameters and observe results.
5. Practice — Solve exercises independently.

## Learning Objectives

By completing this repository, I aim to:

- Understand PyTorch from fundamentals to advanced concepts.
- Understand the mathematics behind deep learning.
- Build neural networks from scratch.
- Implement and compare different optimizers.
- Train and evaluate deep learning models.
- Develop computer vision and medical image analysis projects.
- Conduct independent deep learning research.

## Official Resources

- [PyTorch Official Website](https://pytorch.org/)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Torchvision Documentation](https://pytorch.org/vision/stable/index.html)

---

**Learning by Understanding, Implementing, and Experimenting.**

*This repository is continuously updated as I progress from basic to advanced PyTorch concepts.*
