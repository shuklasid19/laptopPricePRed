#read the data from the data source
#save it in the data/raw for further process
# load the train and test
# train algo
# save the metrices, params
# 


from random import random
import warnings
import sys
import pandas as pd
import numpy as np
import os
import joblib

from sklearn.compose import ColumnTransformer
from get_data import read_params, get_data
import argparse
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn import metrics
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn import tree
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import os
import json
from urllib.parse import urlparse


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    n_estimators=config["estimators"]["RandomForestRegressor"]["params"]["n_estimators"]
    random_state=config["estimators"]["RandomForestRegressor"]["params"]["random_state"]
    max_samples=config["estimators"]["RandomForestRegressor"]["params"]["max_samples"]
    max_features=config["estimators"]["RandomForestRegressor"]["params"]["max_features"]
    max_depth=config["estimators"]["RandomForestRegressor"]["params"]["max_depth"]

    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")

    X_train, X_test, y_train, y_test = train_test_split(train,test,
             test_size=split_ratio,random_state=random_state)
      
########################################################################


    rf1 = RandomForestRegressor(n_estimators=n_estimators,
                              random_state=random_state,
                              max_samples=max_samples,
                              max_features=max_features,
                              max_depth=max_depth) 

    rf1.fit(X_train, y_train.values.ravel())

    predicted_qualities = rf1.predict(X_test)
        
    (rmse, mae, r2) = eval_metrics(y_test.values.ravel(), predicted_qualities)

    print("RandomForestRegression (n_estimators=%d, random_state=%d ,max_samples=%f,  max_features=%f,  max_depth=%d):" % (n_estimators, random_state,  max_samples, max_features, max_depth))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)


    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]
    
    with open(scores_file, "w") as f:
        scores = {
            "rmse":rmse,
            "mae" : mae,
            "r2" : r2
        }
        json.dump(scores, f, indent=4)
   
    with open(params_file , "w") as f:
        params = {
            "n_estimators":n_estimators,
            "random_state": random_state,
            "max_samples": max_samples,
            "max_features":max_features,
            "max_depth" : max_depth
        }
        json.dump(params, f, indent=4)

   

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(rf1, model_path)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
    
  




    