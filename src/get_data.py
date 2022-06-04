import yaml
import argparse
import pandas as pd


def read_params(config_path):
    with open(config_path, 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    config = read_params(config_path)
    # print(config)
    given_data_path = config['data_source']['s3_source']
    df = pd.read_csv(given_data_path, sep=',', encoding='utf-8')
    # print(df.head())
    return df


if __name__ == "__main__":
    args = argparse.ArgumentParser(description="Configuration parameters for the project")
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)
