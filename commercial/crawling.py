import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import json


def getJuDanDaeLoanData():
    res = requests.get("http://ecos.bok.or.kr/api/StatisticSearch/UK7OYPB8FWIWM5LLJFYH/json/kr/1/10/008Y002/MM/202001/202007/11100A0/")
    soup = bs(res.text, "html.parser")
    req = json.loads(soup.text)
    result = pd.DataFrame(req['StatisticSearch']['row'])
    data_list = []
    data_list.append(result['DATA_VALUE'])
    data_list.append(result['TIME'])
    return data_list