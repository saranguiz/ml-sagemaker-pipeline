import json
import logging
import sys
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.models import resnext101_32x8d
import torchvision.transforms as transforms
from PIL import Image
import io
import requests
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))
JSON_CONTENT_TYPE = 'application/json'


def net():
    model = resnext101_32x8d(pretrained=True)

    for param in model.parameters():
        param.requires_grad = False

    num_features = 5
    model.fc = nn.Sequential(
                   nn.Linear(2048, 128),
                   nn.ReLU(inplace=True),
                   nn.Linear(128, num_features))
    return model


def model_fn(model_dir):
    print("In model_fn. Model directory is -")
    print(model_dir)
    model = net()
    with open(os.path.join(model_dir, "model.pth"), "rb") as f:
        logger.info('Loading the model')
        checkpoint = torch.load(f)
        model.load_state_dict(checkpoint)
        logger.info('model loaded successfully')
    model.eval()
    return model


# process a URL submitted to the endpoint
def input_fn(request_body, content_type=JSON_CONTENT_TYPE):
    logger.info('Deserializing the input data.')
    logger.debug(f'Request body CONTENT-TYPE is: {content_type}')
    logger.debug(f'Request body TYPE is: {type(request_body)}')
    if content_type == JSON_CONTENT_TYPE:
        #img_request = requests.get(url)
        logger.debug(f'Request body is: {request_body}')
        request = json.loads(request_body)
        logger.debug(f'Loaded JSON object: {request}')
        url = request['url']
        img_content = requests.get(url).content
        return Image.open(io.BytesIO(img_content))
    else:
        raise Exception('Requested unsupported ContentType in content_type: {}'.format(content_type))

# inference
def predict_fn(input_object, model):
    logger.info('In predict fn')
    test_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    ])
    logger.info("transforming input")
    input_object=test_transform(input_object)
    
    with torch.no_grad():
        logger.info("Calling model")
        prediction = model(input_object.unsqueeze(0))
    return prediction
