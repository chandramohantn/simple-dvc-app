import os
import json
import joblib
import argparse
import pandas as pd
from get_data import read_params
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def eval_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mse, mae, r2

def train_and_evaluate(config_path):
    config = read_params(config_path)
    train_data_path = config['split_data']['train_path']
    test_data_path = config['split_data']['test_path']
    random_seed = config['base']['random_state']
    target_col = config['base']['target_col']
    model_path = config['model_dir']
    alpha = config['estimators']['ElasticNet']['params']['alpha']
    l1_ratio = config['estimators']['ElasticNet']['params']['l1_ratio']

    train = pd.read_csv(train_data_path)
    test = pd.read_csv(test_data_path)
    train_y = train[target_col]
    test_y = test[target_col]
    train_x = train.drop(target_col, axis=1)
    test_x = test.drop(target_col, axis=1)

    lr = ElasticNet(
        alpha=alpha, 
        l1_ratio=l1_ratio, 
        random_state=random_seed
    )
    lr.fit(train_x, train_y)

    predicted_quality = lr.predict(test_x)
    mse, mae, r2 = eval_metrics(test_y, predicted_quality)

    print('ElasticNet model (alpha: %f , l1_ratio: %f)' % (alpha, l1_ratio))
    print('MSE: %f' % mse)
    print('MAE: %f' % mae)
    print('R2: %f' % r2)

    params_file = config['reports']['params']
    scores_file = config['reports']['scores']

    with open(params_file, 'w') as f:
        params = {
            'alpha': alpha,
            'l1_ratio': l1_ratio
        }
        json.dump(params, f, indent=4)

    with open(scores_file, 'w') as f:
        scores = {
            'mse': mse,
            'mae': mae,
            'r2_score': r2
        }
        json.dump(scores, f, indent=4)

    os.makedirs(model_path, exist_ok=True)
    model_dir = os.path.join(model_path, "model.joblib")
    joblib.dump(lr, model_dir)


if __name__ == "__main__":
    args = argparse.ArgumentParser(description="Configuration parameters for the project")
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
