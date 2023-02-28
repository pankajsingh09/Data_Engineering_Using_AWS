import boto3
import requests

s3_client = boto3.client('s3')

# s3_objects = s3_client.list_objects(
#     Bucket='itv-test-github'
# )

file = '2021-01-29-0.json.gz'
res = requests.get(f'https://data.gharchive.org/{file}')

# print(s3_objects)

upload_res = s3_client.put_object(
    Bucket='itv-test-github',
    Key='2021-01-29-0.json.gz',
    Body=res.content
)

print(upload_res)
