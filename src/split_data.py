import argparse
import pandas as pd
from get_data import read_params
from sklearn.model_selection import train_test_split


def split_and_save(config_path):
    config = read_params(config_path)
    train_data_path = config['']['']
    df = get_data(config_path)
    new_cols = [col.replace(" ", "_") for col in list(df)]
    df.to_csv(raw_data_path, sep=',', index=False, encoding='utf-8', headers=new_cols)


if __name__ == "__main__":
    args = argparse.ArgumentParser(description="Configuration parameters for the project")
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    split_and_save(config_path=parsed_args.config)