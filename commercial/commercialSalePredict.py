import joblib
import lightgbm as lgb
from sklearn import preprocessing
import numpy as np
import pandas as pd
def getPredictResult(service_name, location_name, selected_data):
    load_model = joblib.load("../finalProject/finalProject/static/commercial/model/commercialPredict.pkl")
    le1 = preprocessing.LabelEncoder()
    le1.fit(service_name)
    le2 = preprocessing.LabelEncoder()
    le2.fit(location_name)
    fixed_data = [2020,3,le2.transform(selected_data['COMMERCIAL_NAME']), selected_data['AVERAGE_INCOME'], selected_data['CONSUM_TOTAL'],\
                  selected_data['BUSIPOP'],selected_data['FPOP'],selected_data['ALPOP'],selected_data['TOTAL_POP'],\
                  le1.transform(selected_data['SERVICE_NAME']),selected_data['CLOSE_RATIO'],selected_data['SHOPN'],selected_data['NUMBER_OF_PAYMENT']]
    forpredict = np.array([fixed_data])
    return load_model.predict(forpredict)[0]