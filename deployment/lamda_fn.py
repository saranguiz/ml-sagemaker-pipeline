import logging
import json
import boto3
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

print('Loading Lambda function')

runtime=boto3.Session().client('sagemaker-runtime')
endpoint_Name='object-counting-endpoint'

def lambda_handler(event, context):

    print('Context: ',context)
    print('EventType: ',type(event))
    print('Event body: ', event['body'])
    body = json.dumps(event['body'])
    
    runtime=boto3.Session().client('sagemaker-runtime')
    response=runtime.invoke_endpoint(EndpointName=endpoint_Name,
                                    ContentType="application/json",
                                    Accept='application/json',
                                    Body=json.loads(body))
                                    
    result=response['Body'].read().decode('utf-8')
    preds=json.loads(result)
    labeled_predictions = list(zip(range(5), preds[0]))
    print("Labeled predictions: ", labeled_predictions)
    
    labeled_predictions.sort(key=lambda label_and_prob: 1.0 - label_and_prob[1])
    likely_answer = "Most likely answer: there is {} object(s) in the bin".format(labeled_predictions[0][0]+1)
    
    return {
        'statusCode': 200,
        'headers' : { 'Content-Type' : 'text/plain', 'Access-Control-Allow-Origin' : '*' },
        'body' : likely_answer 
        }
