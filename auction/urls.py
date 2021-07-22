from django.urls import path
from . import views

urlpatterns =[
    path("list",views.list),
    path("list_sel",views.list_sel),
    path("list_sel_cnt",views.list_sel_cnt),
    path("list_sel_detail",views.list_sel_detail),
    path("list_ip_ins",views.list_ip_ins),
]