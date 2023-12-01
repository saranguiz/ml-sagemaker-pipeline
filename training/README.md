The scripts used in this project are based on an image classifier implemented with Pytorch that makes use of pretrained models that can be fine-tuned on a custom dataset.

## Pre-requisites

- Python version `3.6` or greater

- Libraries: `torch`, `torchvision`, `argparse`, `Pillow` (can be installed with `pip`)

## Model

As a result of the [models benchmark](../benchmark/README.md), the `train` script was implemented to work with a `ResNeXt-101` model imported from the Pytorch's torchvision library. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```model = resnext101_32x8d(weights=ResNeXt101_32X8D_Weights.DEFAULT)```

Loss function: [`CrossEntropyLoss`](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)

## Classifier

- The number of categories is set in this line:

    ```num_features = 5```

- While the model gets trained, its loss and accuracy gets evaluated during the training and validation phase.

- The model is saved only if the validation accuracy is higher than in previous epochs.

- Testing is done at the end with the model version that best performed in the validation phase. Testing loss and accuracy is calculated against a subset never seen before.

## Dataset

- The main data folder and the train script must be in the same directory
- The images used for training, validation and testing must be in their respective sub-folders ordered by categories.

    ```
    |-- data_dir
    |   |-- test
    |   |   |-- 1
    |   |   |-- 2
    |   |   |-- 3
    |   |   |-- 4
    |   |   |-- 5
    |   |-- train
    |   |   |-- 1
    |   |   |-- 2
    |   |   |-- 3
    |   |   |-- 4
    |   |   |-- 5
    |   |-- valid
    |   |   |-- 1
    |   |   |-- 2
    |   |   |-- 3
    |   |   |-- 4
    |   |   |-- 5
    ```

- For splitting the dataset into testing, training and validation subsets, the [`split-folders`](https://github.com/jfilter/split-folders) library was very helpful.

## Scripts variants

### train.py
Base script that can run locally in any machine. I'd suggest to run experiments with a minimal dataset in a first stage. This way results of the model training are very quick and one gets familiar with the training algorithm for future debugging or enhancements. Source of the project: [pytorch-image-classifier](https://github.com/saranguiz/pytorch-image-classifier)

To run locally: 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```python3 train.py ./data_dir --epochs [N] --lr [LR] --batch_size [BS]```

### hpo.py
Script to be used specifically for Hyperparameter Optimization. It's based on `train.py` and has the ability to access environment variables that AWS Sagemaker uses. Also, a few adjustment has been made to add logging functionality and work with AWS Sagemaker configuration and cloud environment.

### train_debug.py
Script to be used specifically for Debugging and Profiling. It's based on `hpo.py` and implements hooks for debugging and profiling both training and validation phases.
