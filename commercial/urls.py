"""finalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="home"),
    path('gologin', views.gologin, name="gologin"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('goProduct', views.goProduct, name="goProduct"),
    path('goAnalysis', views.goAnalysis, name="goAnalysis"),
    path('goAnalysisCommercial', views.goAnalysisCommercial, name="goAnalysisCommercial"),
    path('goAnalysisApart', views.goAnalysisApart, name="goAnalysisApart"),
    path('goMyPage', views.goMyPage, name="goMyPage"),
    path('mypage_info', views.mypage_info, name="mypage_info"),
    path('getCardDataForGuName', views.getCardDataForGuName, name="getCardDataForGuName"),
    path('getCardDataForDongName', views.getCardDataForDongName, name="getCardDataForDongName"),
    path('goCommercialResult', views.goCommercialResult, name="goCommercialResult"),
    path('getJuDamDataData', views.getJuDamLoanData, name="getJuDamLoanData"),
    path('goCalc', views.goCalc, name="goCalc"),
    path('getPriceCalc', views.getPriceCalc, name="getPriceCalc"),
    path('inheritTaxCalc', views.inheritTaxCalc, name="inheritTaxCalc"),
    path('mypage_comulist', views.mypage_comulist , name="mypage_comulist"),
    path('mypage_customer', views.mypage_customer , name="mypage_customer"),
    path('mypage_MOBI', views.mypage_MOBI, name="mypage_MOBI"),
    path('mypage_MOBI2', views.mypage_MOBI2, name="mypage_MOBI2"),
    path('goDetail', views.goDetail, name="goDetail"),
    path('commu_detail_form', views.commu_detail_form, name="commu_detail_form"),
    path('goCustor_Detail', views.goCustor_Detail, name="goCustor_Detail"),
    path('customer_detail_form', views.customer_detail_form, name="customer_detail_form"),
    path("mypageauction",views.mypageauction, name="mypageauction"),
    path('goAnalysisApartment', views.goAnalysisApartment, name="goAnalysisApartment"),
    path('goAnalysisApartmentResult', views.goAnalysisApartmentResult, name="goAnalysisApartmentResult"),
    path('predictCommercialSale', views.predictCommercialSale, name="predictCommercialSale"),
    path('getApartName', views.getApartName, name="getApartName"),
    path('getRealDealPrice', views.getRealDealPrice, name='getRealDealPrice'),
    path('getExclusiveArea', views.getExclusiveArea, name='getExclusiveArea'),
]
