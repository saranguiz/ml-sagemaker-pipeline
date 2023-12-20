# AWS Sagemaker pipeline for object counting

## Summary

Efficient inventory management is the cornerstone of successful distribution centers. As the items handling process becomes increasingly automated, counting objects in stock or delivery bins has emerged as a technical challenge. To address this, the potential of Computer Vision and Machine Learning offer a promising solution to the challenges of analyzing images and accurately count objects.

This project is the final assessment to complete the AWS Machine Learning Engineer Nanodegree at Udacity. See more details in the project's [proposal](./proposal.pdf) and [report](./report.pdf) documents.

## ML Pipeline on AWS Sagemaker
The technical implementation of the engineering pipeline on [AWS Sagemaker](https://aws.amazon.com/sagemaker/) is presented on the project’s core notebook: 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**[sagemaker.ipynb](./sagemaker.ipynb)** 

The details of each step of the ML pipeline are described in the following sections:
* Dataset EDA ([see notebook](./data_prep/Dataset_EDA.ipynb))
* Models benchmark ([see notebook](./models_benchmark/Models_benchmark.ipynb))
* Training, validation and testing ([see section](./training/README.md))
    * Model used for image classification
    * Dataset split
    * Hyperparameter Optimization script
    * Debugging and profiling script
* Deployment and inference ([see section](./deployment/README.md))

## Image prediction
End-users of the system can invoke the production endpoint and query the prediction of images on [this website](https://sebastian.aranguiz.de/ml/predict):

![image](./deployment/ui/ui.png)

## Contact
📫 How to reach me: [sebastian.aranguiz.de](https://sebastian.aranguiz.de/) 
