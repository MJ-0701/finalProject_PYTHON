import joblib
import lightgbm as lgb
from sklearn import preprocessing
import numpy as np
import pandas as pd
import os
def getApartmentPredictResult(apartmentId, dongName, exclusive_use_area, year_of_completion, floor, dong_name_list):
    load_model = joblib.load("../finalProject/finalProject/static/commercial/model/apartmentPredict.pkl")
    le1 = preprocessing.LabelEncoder()
    le1.fit(dong_name_list)
    fixed_data = [apartmentId, le1.transform([dongName]),exclusive_use_area ,year_of_completion, 202009, floor]
    forpredict = np.array([fixed_data])
    return load_model.predict(forpredict)[0]