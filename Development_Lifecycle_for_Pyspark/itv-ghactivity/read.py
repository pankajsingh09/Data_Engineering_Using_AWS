def from_files(spark, data_dir, file_pattern, file_format):
    df = spark.read. \
        format(file_format). \
        load(f'{data_dir}/{file_pattern}')
    return df
