# Deep Learning Experiments

This document provides a structured framework for tracking, documenting, and comparing Deep Learning experiments conducted using PyTorch.

The objective is to maintain reproducibility, evaluate model performance, and systematically analyze experimental results.

## 1. Experiment Overview

Each experiment should have a unique Experiment ID and document the following information:

- Experiment ID
- Experiment Name
- Date
- Research Objective
- Dataset
- Model Architecture
- Optimizer
- Learning Rate
- Batch Size
- Number of Epochs
- Loss Function
- Evaluation Metrics
- Experimental Results

## 2. Experiment Tracking

Use the following table to maintain an overview of experiments.

| Experiment ID | Model | Dataset | Optimizer | Learning Rate | Batch Size | Status |
|---|---|---|---|---|---|---|
| EXP-001 | CNN | MNIST | Adam | 0.001 | 32 | Completed |
| EXP-002 | MLP | MNIST | SGD | 0.01 | 64 | Completed |
| EXP-003 | ResNet18 | CIFAR-10 | AdamW | 0.0001 | 32 | Planned |
| EXP-004 | U-Net | Brain MRI | Adam | 0.0001 | 16 | Planned |

*Note: These are illustrative examples, not verified experimental results.*

## 3. Experimental Configuration

Record the configuration used in each experiment.

| Parameter | Description |
|---|---|
| Framework | PyTorch |
| Programming Language | Python |
| Hardware | CPU / GPU |
| CUDA Version | Specify CUDA version |
| Dataset | Dataset name and version |
| Model | Model architecture |
| Optimizer | SGD / Adam / AdamW |
| Learning Rate | Initial learning rate |
| Batch Size | Training batch size |
| Epochs | Total training epochs |
| Loss Function | Selected loss function |
| Random Seed | Reproducibility seed |

## 4. Model Performance Evaluation

Evaluate models using appropriate metrics depending on the task.

### Classification

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix

### Image Segmentation

- Dice Similarity Coefficient (DSC)
- Intersection over Union (IoU)
- Hausdorff Distance (HD95)
- Precision
- Recall

### Regression

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## 5. Experiment Results

Record the final performance of each experiment.

| Experiment ID | Model | Accuracy | Precision | Recall | F1-Score | Notes |
|---|---|---|---|---|---|---|
| EXP-001 | CNN | TBD | TBD | TBD | TBD | Baseline |
| EXP-002 | MLP | TBD | TBD | TBD | TBD | Baseline |
| EXP-003 | ResNet18 | TBD | TBD | TBD | TBD | Architecture comparison |

*Replace TBD with actual experimental results.*

## 6. Hyperparameter Experiments

Track the effects of different hyperparameter configurations.

| Experiment ID | Optimizer | Learning Rate | Batch Size | Weight Decay |
|---|---|---|---|---|
| HP-001 | Adam | 0.001 | 32 | 0.0001 |
| HP-002 | Adam | 0.0001 | 32 | 0.0001 |
| HP-003 | AdamW | 0.001 | 64 | 0.01 |
| HP-004 | SGD | 0.01 | 32 | 0.0001 |

## 7. Reproducibility Guidelines

To improve experimental reproducibility:

- Set random seeds.
- Record software and hardware versions.
- Document dataset preprocessing.
- Save model configurations.
- Record training and validation results.
- Keep track of optimizer and scheduler settings.
- Maintain experiment logs and checkpoints.

## 8. Experiment Directory Structure

Organize experimental files using a consistent directory structure.

```text
experiments/
│
├── EXP-001_CNN_MNIST/
│   ├── config.yaml
│   ├── train.py
│   ├── results.csv
│   └── README.md
│
├── EXP-002_MLP_MNIST/
│   ├── config.yaml
│   ├── train.py
│   ├── results.csv
│   └── README.md
│
└── EXP-003_ResNet_CIFAR10/
    ├── config.yaml
    ├── train.py
    ├── results.csv
    └── README.md
```

## 9. Experiment Reporting Template

Use this template to document individual experiments.

### Experiment ID: EXP-XXX

**Experiment Name:**

**Objective:**

**Dataset:**

**Model Architecture:**

**Experimental Configuration:**

| Parameter | Value |
|---|---|
| Optimizer | |
| Learning Rate | |
| Batch Size | |
| Epochs | |
| Loss Function | |
| Random Seed | |

**Results:**

| Metric | Training | Validation | Test |
|---|---|---|---|
| Loss | | | |
| Accuracy | | | |
| F1-Score | | | |

**Observations:**

**Conclusion:**

**Future Improvements:**

---

## 10. Research Principles

All experiments should follow these principles:

1. Maintain transparent experimental records.
2. Report actual results without fabrication.
3. Use consistent evaluation protocols.
4. Document unsuccessful experiments.
5. Compare models under controlled conditions.
6. Ensure reproducibility whenever possible.

---

**Maintained by:** Md. Arafat Hossain

**Repository:** https://github.com/Arafat-shuvo/PyTorch

**Framework:** PyTorch

**Focus:** Deep Learning | Computer Vision | Neural Networks | Medical Image Analysis
