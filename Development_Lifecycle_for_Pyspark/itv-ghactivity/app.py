import os
from util import get_spark_session
from read import from_files
from process import transform
from write import to_file

def main():
    env = os.environ.get('ENVIRON')
    src_dir = os.environ.get('SRC_DIR')
    src_file_pattern = f'{os.environ.get("SRC_FILE_PATTERN")}-*'
    src_file_format = os.environ.get('SRC_FILE_FORMAT')
    tgt_dir = os.environ.get('TGT_DIR')
    tgt_file_format = os.environ.get('TGT_FILE_FORMAT')

    spark = get_spark_session(env, 'GitHub Activity - Getting Started')
    df = from_files(spark, src_dir, src_file_pattern, src_file_format)

    df_transformed = transform(df)
    to_file(df_transformed,tgt_dir, tgt_file_format)

    print(df_transformed.count())



if __name__ == '__main__':
    main()


