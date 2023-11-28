This script is an image classifier implemented with Pytorch that makes use of pretrained models that can be fine-tuned on a custom dataset.

## Pre-requisites

- Python version `3.9` or greater

- Libraries: `torch`, `torchvision`, `argparse`, `Pillow` (can be installed with `pip`)

## Model

As a result of the [models benchmark](../benchmark/README.md), the `train` script was implemented to work with a `ResNeXt-101` model imported from the Pytorch's torchvision library. 

```model = resnext101_32x8d(weights=ResNeXt101_32X8D_Weights.DEFAULT)```

Loss function: [`CrossEntropyLoss`](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)

## Classifier training

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

## Training execution

From notebook: 



Running locally:

<code>python3 train.py ./data_dir --epochs [N] --lr [LR] --batch_size [BS]</code>
