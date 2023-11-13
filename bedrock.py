import boto3

bedrock = boto3.client(service_name='bedrock', region_name='us-east-1')
listModels = bedrock.list_foundation_models(byProvider='meta')
print("\n".join(list(map(lambda x: f"{x['modelName']} : { x['modelId'] }", listModels['modelSummaries']))))
