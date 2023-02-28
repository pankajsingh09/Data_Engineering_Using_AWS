import os
from download import download_file
from upload import upload_s3


def lambda_handler(event, context):
    file = '2021-01-29-1.json.gz'
    download_res = download_file(file)
    bucket = os.environ.get('BUCKET_NAME')
    bookmark_file = os.environ.get("BOOKMARK_FILE")
    baseline_file = os.environ.get("BASELINE_FILE")
    file_prefix = os.environ.get('FILE_PREFIX')
    environ = os.environ.get('ENVIRON')
    if environ == 'DEV':
        print(f'Running in {environ} environment')
        # os.environ.setdefault('AWS_PROFILE', 'profile_name')
    upload_res = upload_s3(
        download_res.content,
        bucket,
        f'{file_prefix}/{file}'
    )
    return upload_res
