import sys
from typing import io

from bs4 import BeautifulSoup
from django.db import models

# Create your models here.
import cx_Oracle as ora
import pandas as pd
import numpy as np

class Mapper:
    def __init__(self, database):
        self.database = database
    def getUserData(self,  userid):
        conn = ora.connect(self.database)
        sql_select = f"select ANUM,AID,APWD,AINDAY,ACHGDAY,AGUBUN,ADIVISION, DECODE(AGUBUN,'임대인','R','공인중개사','C') as AGUBUN_S from signup where aid = '{userid}'"
        datas = pd.read_sql(sql_select, con=conn)
        conn.close()
        return datas
    def getmemberdata(self, usernum):
        conn = ora.connect(self.database)
        sql_select = f"select s.anum ANUM , s.aid AID , s.apwd APWD , s.ainday AINDAY , s.achgday ACHGDAY , s.agubun AGUBUN , s.adivision ADIVISION , m.dname DNAME ,m.dbirth DBIRTH , m.dgender DGENDER , m.dtel , p.psdate , p.pedate , p.ppay , p.pway , p.pgubun , p.monthnum , pd.kinds , pd.mentnum , pd.inment  from signup s , member_detail m , payment p , payment_detail pd  where s.anum = m.dnum and s.anum = p.pnum and s.anum = pd.pdnum and s.anum = '{usernum}'"
        datas = pd.read_sql(sql_select, con=conn)
        conn.close()
        return datas
    def getGuName(self):
        conn = ora.connect(self.database)
        sql_select = "select distinct sname from writing_tag order by sname"
        datas = pd.read_sql(sql_select, con=conn)

        conn.close()
        return datas

    def getDongName(self, guName):
        conn = ora.connect(self.database)
        sql_select = f"select distinct dong from realdealprice where sigungu ='{guName}' order by dong"
        datas = pd.read_sql(sql_select, con=conn)
        conn.close()
        return datas

    def getcommu_list(self, comunum):
        conn = ora.connect(self.database)
        sql_select = f"select c.wnum , c.wgubun , c.wloc1 , c.wloc2 , c.wtitle , c.wcontents , c.windate , c.wchgdate , c.whit , c.wrec , c.wdel from community_board c , signup s where s.anum = c.anum and c.anum  = '{comunum}'"
        datas = pd.read_sql(sql_select, con=conn)
        conn.close()
        return datas

    def getcommu_detail(self, wnum):
        old_stdout = sys.stdout  # Memorize the default stdout stream
        sys.stdout = buffer = io.StringIO()
        conn = ora.connect(self.database)
        sql_select = f"select c.* from community_board c , signup s where s.anum = c.anum and c.wnum  = '{wnum}'"
        datas = pd.read_sql(sql_select, con=conn)
        a = datas.WCONTENTS.values[0]

        sys.stdout = old_stdout  # Put the old stream back in place
        get_value = buffer.getvalue()  # Return a str containing the entire contents of the   buffer.
        buffer.close()
        bs = BeautifulSoup(get_value, "html.parser")
        bs_value = bs.text.replace("\n", "")
        if bs_value == None:
            datas.WCONTENTS.values[0] = "입력한 내용이 없습니다."
        else:
            datas.WCONTENTS.values[0] = bs_value
        print(datas)
        conn.close()
        return datas

    def getcustomer_list(self, custonum):
        conn = ora.connect(self.database)
        sql_select = f"select c.* from customer_board c , signup s where s.anum = c.anum and c.anum  = '{custonum}'"
        datas = pd.read_sql(sql_select, con=conn)
        return datas

    def gocustomer_detail(self, cnum):
        old_stdout = sys.stdout  # Memorize the default stdout stream
        sys.stdout = buffer = io.StringIO()
        conn = ora.connect(self.database)
        sql_select = f"select c.* from customer_board c , signup s where s.anum = c.anum and c.c_num  = '{cnum}'"
        datas = pd.read_sql(sql_select, con=conn)
        a = datas.C_CONTENT.values[0]
        print(a)
        sys.stdout = old_stdout  # Put the old stream back in place
        get_value = buffer.getvalue()  # Return a str containing the entire contents of the   buffer.
        buffer.close()
        bs = BeautifulSoup(get_value, "html.parser")
        bs_value = bs.text.replace("\n", "")
        if bs_value == None:
            datas.C_CONTENT.values[0] = "입력한 내용이 없습니다."
        else:
            datas.C_CONTENT.values[0] = bs_value
        print(datas)
        conn.close()
        return datas

    def customer_update(self, cnum, csubject, ccontent, ):
        conn = ora.connect(self.database)
        sql_update = f"update customer_board set c_subject = '{csubject}' , c_content = '{ccontent}' where c_num = '{cnum}'"
        cursor = conn.cursor()
        cursor.execute(sql_update)
        conn.commit()
        cursor.close()
        conn.close

    def user_inforupdate(self, usernum, apwd):
        conn = ora.connect(self.database)
        sql_update = f"update signup set apwd ='{apwd}' where anum= '{usernum}'"
        cursor = conn.cursor()
        cursor.execute(sql_update)
        conn.commit()
        cursor.close()
        conn.close

    def user_memberupdate(self, usernum, dname, dtel):
        conn = ora.connect(self.database)
        sql_update = f"update member_detail set dname = '{dname}' , dtel = '{dtel}' where dnum = '{usernum}'"
        cursor = conn.cursor()
        cursor.execute(sql_update)
        conn.commit()
        cursor.close()
        conn.close

    def comu_update(self, wnum, wtitle, wcontents, ):
        conn = ora.connect(self.database)
        sql_update = f"update community_board set wtitle = '{wtitle}' , wcontents = '{wcontents}' , wchgdate = sysdate where wnum = '{wnum}'"
        cursor = conn.cursor()
        cursor.execute(sql_update)
        conn.commit()
        cursor.close()
        conn.close

    def sale(self, aid):
        conn = ora.connect(self.database)
        sql_select = f"select a.anum,a.bid,fn_yongdo_name(a.byongdo) as yongdo,a.baddra as addr,a.bweight,a.tweight,a.hit,b.wimage,b.imagea,b.imageb,b.imagec ,TO_CHAR(p.ideprice,'FM999,999,999,999') as ideprice,p.subject,TO_CHAR(p.enddate,'YYYY-MM-DD HH24:MI:SS') as enddate,TO_CHAR( DECODE(nvl(fn_higt_ipchalper(p.ipnum),0),0,nvl(p.ideprice,0),nvl(fn_higt_ipchalper(p.ipnum),0)),'FM999,999,999,999') as hprice, fn_basedata_name(3,1,p.status) as status,TO_CHAR(a.indate,'YYYY.MM.DD') as indate, DECODE(nvl(fn_higt_ipchalper(p.ipnum),0),0,nvl(p.ideprice,0),nvl(fn_higt_ipchalper(p.ipnum),0)) as inhprice,p.ipnum from actmain a , actmainde b , ipchal p where b.anum = a.anum and p.anum = a.anum  and a.bid =  '{aid}' "
        # datas = pd.read_sql(sql_select, con=conn)
        cursor = conn.cursor()
        cursor.execute(sql_select)
        plist = cursor.fetchall()
        cursor.close()
        conn.close()
        return plist
    def getRealDealPrice(self, dongName):
        conn = ora.connect(self.database)
        sql_select = f"select dongname, year, geowidth, price,buildyear,buildingname,floor from realdealprice where dongname='{dongName}' and yongdo='아파트'"
        datas = pd.read_sql(sql_select, con=conn)
        conn.close()
        return datas
    def getServiceName(self):
        conn = ora.connect(self.database)
        sql_select = "select distinct svc_induty_cd_nm from backbuy "
        datas = pd.read_sql(sql_select, con=conn)
        conn.close()
        return datas
    def getLocationName(self):
        conn = ora.connect(self.database)
        sql_select = "select distinct trdar_cd_nm from backbuy"
        datas = pd.read_sql(sql_select, con=conn)
        conn.close()
        return datas
    def getSelectedData(self,commercial_name,service_name):
        conn = ora.connect(self.database)
        sql_select = f"select * from mergecommercialdata where year = 2020 and commercial_name = '{commercial_name}'and service_name='{service_name}'"
        datas = pd.read_sql(sql_select, con=conn)
        conn.close()
        return datas
    def getApartName(self, guName, dongName):
        conn =ora.connect(self.database)
        sql_select = f"select distinct apt from realdealprice where sigungu = '{guName}' and dong= '{dongName}' order by apt"
        datas = pd.read_sql(sql_select, con=conn)
        print(datas)
        return datas

    def getRealDealPriceData(self, guName, dongName, aptName):
        conn = ora.connect(self.database)
        sql_select = f"select * from realdealprice where sigungu = '{guName}' and dong= '{dongName}' and apt = '{aptName}'"
        datas = pd.read_sql(sql_select, con=conn)
        return datas

    def getLastQuaterTotalSale(self, commercial_name, service_name):
        conn = ora.connect(self.database)
        sql_select = f"select total_sale from merge_commercial_data where commercial_name = '{commercial_name}' and service_name = '{service_name}' and year = 2019 and quater = 3;"
        datas = pd.read_sql(sql_select, con=conn)
        return datas

    def getTotalSaleChange(self):
        conn = ora.connect(self.database)
        sql_select = "select sum(total_sale) from merge_commercial_data where year = 2019 and quater = 4"
        before = pd.read_sql(sql_select, con=conn)
        sql_select = "select sum(total_sale) from merge_commercial_data where year = 2020 and quater = 1"
        after = pd.read_sql(sql_select, con=conn)
        result = (after - before) / after * 100
        return np.floor(result)

    def getChangeSale(self, commercial_name, service_name):
        conn = ora.connect(self.database)
        sql_select = f"select sum(total_sale) from merge_commercial_data where year = 2019 and quater = 4 and commercial_name = '{commercial_name}'and service_name='{service_name}'"
        before = pd.read_sql(sql_select, con=conn)
        sql_select = f"select sum(total_sale) from merge_commercial_data where year = 2020 and quater = 1 and commercial_name = '{commercial_name}'and service_name='{service_name}'"
        after = pd.read_sql(sql_select, con=conn)
        result = (after - before) / after * 100
        result = result.values[0][0]
        if (result >= 20):
            score = 5
        elif (result >= 10):
            score = 4
        elif (result >= 0):
            score = 3
        elif (result >= -10):
            score = 2
        else:
            score = 1
        return score

    def getCommercialAreaScore(self, commercial_name):
        conn = ora.connect(self.database)
        sql_select = "select ((select sum(total_sale) from merge_commercial_data where year = 2020 and quater = 1) - (select sum(total_sale) from merge_commercial_data where year = 2019 and quater = 4)) / (select sum(total_sale) from merge_commercial_data where year = 2019 and quater = 4) * 100 as result from dual"
        all_area = pd.read_sql(sql_select, con=conn)
        sql_select = f"select ((select sum(total_sale) from merge_commercial_data where year = 2020 and quater = 1 and commercial_name = '{commercial_name}') - (select sum(total_sale) from merge_commercial_data where year = 2019 and quater = 4 and commercial_name = '{commercial_name}')) / (select sum(total_sale) from merge_commercial_data where year = 2019 and quater = 4 and commercial_name = '{commercial_name}') * 100 as result from dual"
        selected_area = pd.read_sql(sql_select, con=conn)
        result = selected_area - all_area
        result = result.values[0][0]
        if (result >= 20):
            score = 5
        elif (result >= 10):
            score = 4
        elif (result >= 0):
            score = 3
        elif (result >= -10):
            score = 2
        else:
            score = 1
        return score

    def getPredictGrowthScore(self, commercial_name, service_name, predict_value):
        conn = ora.connect(self.database)
        sql_select = f"select sum(total_sale) from merge_commercial_data where year = 2019 and quater = 3 and commercial_name = '{commercial_name}' and service_name = '{service_name}'"
        datas = pd.read_sql(sql_select, con=conn)
        result = (predict_value / datas) / datas * 100
        result = result.values[0][0]
        if (result >= 20):
            score = 5
        elif (result >= 10):
            score = 4
        elif (result >= 0):
            score = 3
        elif (result >= -10):
            score = 2
        else:
            score = 1
        return score

    def getChangeStoreN(self, commercial_name, service_name):
        conn = ora.connect(self.database)
        sql_select = f"select \
         (select shopn from merge_commercial_data where year=2020 and quater = 1 and commercial_name = '{commercial_name}' and service_name ='{service_name}') -\
          (select shopn from merge_commercial_data where year \
         = 2019 and quater = 4 and commercial_name = '{commercial_name}' and service_name ='{service_name}') as result from dual;"
        datas = pd.read_sql(sql_select, con=conn)
        score = 0
        if (datas > 4 | datas < -4):
            score = 0
        elif (datas > 3 | datas < -3):
            score = 2
        elif (datas > 2 | datas < -2):
            score = 4
        elif (datas > 1 | datas < -1):
            score = 6
        elif (datas > 0 | datas < -0):
            score = 8
        elif (datas == 0):
            score = 10
        return score

    def operationAverage(self, guName):
        conn = ora.connect(self.database)
        sql_select = "select (select max(meanoper) from closebus where year = 2019 and quater = 4) as max,\
         (select min(meanoper) from closebus where year = 2019 and quater = 4) as min from dual"
        datas = pd.read_sql(sql_select, con=conn)
        sql_select = f"select meanoper from closebus where sigungu='{guName}' and year = 2019 and quater = 4"
        result = pd.read_sql(sql_select, con=conn)
        result = result.values[0][0]
        result = (result - datas['MIN'].values[0]) / (datas['MAX'] - datas['MIN'].values[0]) * 5
        return result.values[0]

    def closeRatio(self, commercial_name, service_name):
        conn = ora.connect(self.database)
        sql_select = "select (select max(close_ratio) from merge_commercial_data where year =2020 and quater = 1) as max, \
        (select min(close_ratio) from merge_commercial_data where year =2020 and quater = 1) as min from dual"
        datas = pd.read_sql(sql_select, con=conn)
        sql_select = f"select close_ratio from merge_commercial_data where commercial_name='{commercial_name}' and service_name = '{service_name}' and year = 2020 and quater = 1"
        result = pd.read_sql(sql_select, con=conn)
        result = result.values[0][0]
        result = (result - datas['MIN'].values[0]) / (datas['MAX'] - datas['MIN'].values[0]) * 5
        return result.values[0]

    def consumeIndex(self, commercial_name):
        conn = ora.connect(self.database)
        sql_select = "select avg(average_income) from merge_commercial_data where year = 2020 and quater = 1"
        index = pd.read_sql(sql_select, con=conn)
        index = index.values[0][0]
        sql_select = f"select distinct average_income from merge_commercial_data where year = 2020 and quater = 1 and commercial_name = '{commercial_name}'"
        datas = pd.read_sql(sql_select, con=conn)
        datas = datas.values[0][0]
        if (datas > index):
            score = 5
        else:
            score = 0
        return score

    def getRealDealApart(self, guName, dongName, aptName):
        conn = ora.connect(self.database)
        sql_select = f"select * from realdealprice where sigungu = '{guName}' and dong = '{dongName}' and apt = '{aptName}' and rownum < 6"
        datas = pd.read_sql(sql_select, con=conn)
        return datas

    def getApartFixedData(self, dongName, aptName):
        conn = ora.connect(self.database)
        sql_select = f"select apartment_id, year_of_completion from realdealprice where dong = '{dongName}' and apt='{aptName}' and rownum = 1"
        datas = pd.read_sql(sql_select, con=conn)
        print(datas)
        return datas

    def getDongNameList(self):
        conn = ora.connect(self.database)
        sql_select = "select distinct dong from realdealprice where dong is not null order by dong"
        datas = pd.read_sql(sql_select, con=conn)['DONG'].tolist()
        return datas

    def getExclusiveArea(self, guName, dongName, aptName):
        conn = ora.connect(self.database)
        print(aptName)
        sql_select = f"select distinct EXCLUSIVE_USE_AREA from realdealprice where sigungu = '{guName}' and dong = '{dongName}' and apt='{aptName}'"
        datas = pd.read_sql(sql_select, con=conn)['EXCLUSIVE_USE_AREA'].tolist()
        print(datas)
        return datas