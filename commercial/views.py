from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from . import crawling, commercialSalePredict, apartmentPricePredict
import numpy as np
cardData = "";
from .models import Mapper
# Create your views here.
def index(request):
    if "userid" in request.session:
        return render(request,"index.html", {"id":request.session['userid']})
    else:
        return render(request,"index.html")
def gologin(request):
    return render(request, "login/login.html")
@csrf_exempt
def login(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    id = request.POST.get("Id", "")
    userSession = mapper.getUserData(id)
    if len(userSession) == 0:
        return render(request, "login/login.html", {"id": id})

    request.session["aid"] = userSession["AID"].values[0]
    request.session["agubun_s"] = userSession["AGUBUN_S"].values[0]
    if userSession["APWD"].values[0] == request.POST.get("password",""):
        request.session["userid"] = userSession.to_json()
        return render(request, "index.html",{"session":request.session["userid"]})
    else:
        return render(request, "login/login.html",{"id":id})
def logout(request):
    del request.session["userid"]
    del request.session["aid"]
    del request.session["agubun_s"]
    return redirect("home")
def goProduct(request):
    return render(request, "product/productSearch.html")
def goAnalysis(request):
    return render(request, "analysis/analysisMain.html")
def goAnalysisCommercial(request):
    return render(request, "analysis/analysisCommercial.html")
def goAnalysisApart(request):
    return render(request, "analysis/analysisApart.html")
def getCardDataForGuName(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    guName = mapper.getGuName()['SNAME']
    guName = [x for x in guName]
    return render(request, "server/analysisCommercialTagServer.html",{"data":guName})
def getCardDataForDongName(request):
    guName = request.GET["guName"]
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    dongName = mapper.getDongName(guName)['DONG']
    dongName = [x for x in dongName]
    return render(request, "server/analysisCommercialTagServer.html",{"data":dongName})
def goCommercialResult(request):
    return render(request, "analysis/analysisCommercialResult.html")
def getJuDamLoanData(request):
    result = crawling.getJuDanDaeLoanData()
    return render(request, "server/analysisCommercialServer.html", {"value":result[0],"time":result[1]})
def goCalc(request):
    return render(request, "analysis/taxCalc.html")
def getPriceCalc(request):
    getPrice = request.GET.get('getPrice')
    getTax = int(getPrice) * 0.04
    specialTax = int(getPrice) * 0.002
    eduTax = int(getPrice) * 0.004
    totalTax = int(getPrice) * 0.046
    result = [int(getPrice), int(getTax), int(specialTax), int(eduTax), int(totalTax)]
    return render(request, "server/calcServer.html", {"result":result,"length":len(result)})
def inheritTaxCalc(request):
    getPrice = int(request.GET.get('getPrice'))
    if getPrice <= 100000000:
        tax_ratio = 0.1
        deductible = 0
    elif  getPrice <= 500000000:
        tax_ratio = 0.2
        deductible = 10000000
    elif getPrice <= 1000000000:
        tax_ratio = 0.3
        deductible = 6000000
    elif getPrice <= 3000000000:
        tax_ratio = 0.4
        deductible = 16000000
    elif getPrice > 3000000000:
        tax_ratio = 0.5
        deductible = 46000000
    total = getPrice * tax_ratio - deductible
    result = [getPrice, int(tax_ratio*100), deductible, total]
    return render(request, "server/calcServer.html", {"result":result,"length":len(result)})

def goMyPage(request):
    print("확인", request.GET.get("anum", ""))
    if request.GET.get("anum", "") == "":
        return render(request, "login/login.html")
    else:
        return render(request, "mypage/mypage.html")

@csrf_exempt
def mypage_info(request):
    mapper = Mapper("semiproejct/kosmo@localhost:1521/orcl")
    user_infor = mapper.getmemberdata(request.POST.get("user_NUM", ""))
    user_infor['AINDAY'] = user_infor['AINDAY'].astype(str)
    user_infor['ACHGDAY'] = user_infor['ACHGDAY'].astype(str)
    user_infor['PEDATE'] = user_infor['PEDATE'].astype(str)
    user_infor['PSDATE'] = user_infor['PSDATE'].astype(str)
    user_infor['DBIRTH'] = user_infor['DBIRTH'].astype(str)
    user_data = user_infor.to_json()
    return render(request, "mypage/user_infor.html", {"userinfor": user_data})

@csrf_exempt
def mypage_comulist(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    user_community_list = mapper.getcommu_list(request.POST.get("user_NUM", ""))
    user_community_list['WINDATE'] = user_community_list['WINDATE'].astype(str)
    community_datas = user_community_list.to_json()
    return render(request, "mypage/community_list.html", {"comudata": community_datas})

@csrf_exempt
def mypage_customer(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    user_customer_list = mapper.getcustomer_list(request.POST.get("user_NUM", ""))
    user_customer_list['C_REGDATE'] = user_customer_list['C_REGDATE'].astype(str)
    customer_datas = user_customer_list.to_json()
    return render(request, "mypage/customer_list.html", {"customerdata": customer_datas})

@csrf_exempt
def mypage_MOBI(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    print("anum : " + request.POST.get("anum", ""))
    print("apwd : " + request.POST.get("apwd", ""))
    mapper.user_inforupdate(request.POST.get("anum", ""), request.POST.get("apwd", ""))
    user_infor = mapper.getmemberdata(request.POST.get("anum", ""))
    user_infor['AINDAY'] = user_infor['AINDAY'].astype(str)
    user_infor['ACHGDAY'] = user_infor['ACHGDAY'].astype(str)
    user_infor['PEDATE'] = user_infor['PEDATE'].astype(str)
    user_infor['PSDATE'] = user_infor['PSDATE'].astype(str)
    user_infor['DBIRTH'] = user_infor['DBIRTH'].astype(str)
    user_data = user_infor.to_json()
    return render(request, "mypage/user_infor.html", {"userinfor": user_data})

@csrf_exempt
def mypage_MOBI2(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    mapper.user_memberupdate(request.POST.get("anum2", ""), request.POST.get("dname", ""),
                                 request.POST.get("dtel", ""))
    user_infor = mapper.getmemberdata(request.POST.get("anum2", ""))
    user_infor['AINDAY'] = user_infor['AINDAY'].astype(str)
    user_infor['ACHGDAY'] = user_infor['ACHGDAY'].astype(str)
    user_infor['PEDATE'] = user_infor['PEDATE'].astype(str)
    user_infor['PSDATE'] = user_infor['PSDATE'].astype(str)
    user_infor['DBIRTH'] = user_infor['DBIRTH'].astype(str)
    user_data = user_infor.to_json()
    return render(request, "mypage/user_infor.html", {"userinfor": user_data})

def goDetail(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    user_community_list = mapper.getcommu_detail(request.GET.get("wnum", ""))
    user_community_list['WINDATE'] = user_community_list['WINDATE'].astype(str)
    community_datas = user_community_list.iloc[0, :].to_dict()
    return render(request, "mypage/community_detail.html", {"comudata": community_datas})

@csrf_exempt
def commu_detail_form(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    mapper.comu_update(request.POST.get("wnum", ""), request.POST.get("wtitle", ""),
    request.POST.get("wcontents", ""))
    user_community_list = mapper.getcommu_list(request.POST.get("anum", ""))
    user_community_list['WINDATE'] = user_community_list['WINDATE'].astype(str)
    community_datas = user_community_list.to_json()
    return render(request, "mypage/community_list.html", {"comudata": community_datas})

@csrf_exempt
def customer_detail_form(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    mapper.customer_update(request.POST.get("cnum", ""), request.POST.get("c_subject", ""),
    request.POST.get("c_content", ""))
    user_customer_list = mapper.getcustomer_list(request.POST.get("anum", ""))
    user_customer_list['C_REGDATE'] = user_customer_list['C_REGDATE'].astype(str)
    customer_datas = user_customer_list.to_json()
    return render(request, "mypage/customer_list.html", {"customerdata": customer_datas})

def goCustor_Detail(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    user_customer_list = mapper.gocustomer_detail(request.GET.get("cnum", ""))
    user_customer_list['C_REGDATE'] = user_customer_list['C_REGDATE'].astype(str)
    customer_datas = user_customer_list.to_json()
    return render(request, "mypage/customer_detail.html", {"customerdata": customer_datas})

@csrf_exempt
def mypageauction(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    sale = mapper.sale(request.POST.get("user_AID", ""))
    # sale_data = sale.to_json()
    return render(request, "mypage/auction_sale.html", {"sale": sale})

def goAnalysisApartment(request):
    return render(request, "analysis/analysisApartment.html")

@csrf_exempt
def goAnalysisApartmentResult(request):
    selectedChart = request.POST.getlist("selectedChart[]")
    guName = request.POST['guName']
    dongName = request.POST['dongName']
    aptName = request.POST['apartName'] #설립년도 정보와 아파트 아이디정보를 가져와야함 해당 정보를 통해서 가져온 값으로 모델에 넣을 것.
    floor = request.POST["floor"]
    exclusive_use_area = request.POST['exclusive_use_area']
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    datas = mapper.getApartFixedData(dongName, aptName)
    print(datas)
    apartmentId = datas['APARTMENT_ID'].values[0]
    year_of_completion = datas['YEAR_OF_COMPLETION'].values[0]
    dong_name_list = mapper.getDongNameList()
    predict_value = apartmentPricePredict.getApartmentPredictResult(apartmentId=apartmentId, \
                                                                    dongName=dongName, exclusive_use_area=exclusive_use_area,year_of_completion=\
                                                                        year_of_completion,floor= floor,dong_name_list= dong_name_list)
    predict_value = trunc(predict_value)
    return render(request, "analysis/analysisApartMentResult.html", {"selectedChart":selectedChart,"guName":guName ,"dongName":dongName, "aptName":aptName,"predict_value":predict_value})

def getRealDealPriceData(request):
    dongName = request.GET['dongName']
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    data = mapper.getRealDealPriceData(dongName)
    return render(request, "analysis/analysisApartmentResult.html", {"realDealData":data})

def predictCommercialSale(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    guName = request.GET.get('guName')
    commercial_name = request.GET['commercial_name']
    service_name = request.GET['service_name']
    location_name_list = mapper.getLocationName()
    service_name_list = mapper.getServiceName()
    selected_data = mapper.getSelectedData(commercial_name=commercial_name, service_name=service_name)
    result = commercialSalePredict.getPredictResult(service_name=service_name_list, location_name=location_name_list, selected_data =selected_data)
    result = int(np.round(result, -3))
    result_data = dict()
    result_data['prdictValue'] = result
    saleChange = mapper.getChangeSale(commercial_name, service_name)
    result_data['saleChange'] = saleChange
    commercial_ratio = mapper.getCommercialAreaScore(commercial_name)
    result_data['commercialRatio'] = commercial_ratio
    predictGrowthScore = mapper.getPredictGrowthScore(commercial_name,service_name, result)
    result_data['predictGrowthScore'] = predictGrowthScore
    operationAverage = mapper.operationAverage(guName)
    result_data['operationAverage'] = operationAverage
    closeRatio = mapper.closeRatio(commercial_name, service_name)
    result_data['closeRatio'] = closeRatio
    consumeIndex = mapper.consumeIndex(commercial_name)
    result_data['consumeIndex'] = consumeIndex
    return render(request,'server/commercialSalePredict.html',{"result":result_data})

def getApartName(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    guName = request.GET['guName']
    dongName = request.GET['dongName']
    apartName = mapper.getApartName(guName,dongName)['APT']
    apartName = [x for x in apartName]
    return render(request, "server/analysisCommercialTagServer.html", {"data": apartName})

def getRealDealPrice(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    guName = request.GET.get('guName')
    dongName = request.GET.get('dongName')
    aptName = request.GET.get('aptName')
    print(guName,dongName,aptName)
    result = mapper.getRealDealApart(guName, dongName, aptName)
    print(result)
    result = result.iloc[:,[-2,2,3,4,7,-1]]
    result = result.T.to_dict()
    resultlist = []
    for e in result:
        resultlist.append(result[e])
    return render(request,"server/realDealPriceTable.html", {"resultlist":resultlist})

def getExclusiveArea(request):
    mapper = Mapper("semiproject/kosmo@localhost:1521/orcl")
    guName = request.GET['guName']
    dongName = request.GET['dongName']
    aptName = request.GET['aptName']
    result = mapper.getExclusiveArea(guName, dongName, aptName)
    return render(request, "server/analysisCommercialTagServer.html",{"data":result})

def trunc(value):
    return int(np.trunc(value/1000)*1000)