from django.shortcuts import render, redirect
import cx_Oracle as ora
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

#(5, 'test1', '아파트', '서울특별시 금천구 금하로30길 34, 1705 (시흥동, 탑스빌아파트)', 111, 222, 103, 'g4.jpg', '30,000', 'test입니다', '2020-06-08 05:24:', '5,555,555', '낙찰', '2020.06.05'),
def list(request):
    conn = ora.connect('semiproject/kosmo@localhost:1521/orcl')
    list_sql = "select * from("
    list_sql += "select T.*,rownum as r_num from("
    list_sql += "select a.anum,a.bid,fn_yongdo_name(a.byongdo) as yongdo,a.baddra as addr,a.bweight,a.tweight,a.hit,b.wimage"
    list_sql += ",TO_CHAR(p.ideprice,'FM999,999,999,999') as ideprice,p.subject,TO_CHAR(p.enddate,'YYYY-MM-DD HH24:MI:') as enddate"
    list_sql += ",TO_CHAR( DECODE(nvl(fn_higt_ipchalper(p.ipnum),0),0,nvl(p.ideprice,0),nvl(fn_higt_ipchalper(p.ipnum),0)),'FM999,999,999,999') as hprice"
    list_sql += ", fn_basedata_name(3,1,p.status) as status,TO_CHAR(a.indate,'YYYY.MM.DD') as indate "
    list_sql += "from actmain a , actmainde b , ipchal p "
    list_sql += "where b.anum = a.anum and p.anum = a.anum"
    list_sql += ") T ) where r_num between 1 and 10 "

    # palist = pd.read_sql(list_sql,con=conn)
    # alist = palist.to_dict()
    cursor = conn.cursor()
    cursor.execute(list_sql)
    alist = cursor.fetchall()
    cursor.close()
    return render(request, "auction/auction_list.html", {"alist": alist,"asp":1,"aed":10,"aorder":0,"pcnt":1})

def list_sel(request):
    conn = ora.connect('semiproject/kosmo@localhost:1521/orcl')

    sp = request.GET["sp"]
    ep = request.GET["ep"]
    orderby = request.GET["orderby"]
    pcnt = request.GET["pcnt"]

    print("sp:",sp,"ep:",ep)
    list_sql = "select * from("
    list_sql += "select T.*,rownum as r_num from("
    list_sql += "select a.anum,a.bid,fn_yongdo_name(a.byongdo) as yongdo,a.baddra as addr,a.bweight,a.tweight,a.hit,b.wimage"
    list_sql += ",TO_CHAR(p.ideprice,'FM999,999,999,999') as ideprice,p.subject,TO_CHAR(p.enddate,'YYYY-MM-DD HH24:MI:') as enddate"
    list_sql += ",TO_CHAR( DECODE(nvl(fn_higt_ipchalper(p.ipnum),0),0,nvl(p.ideprice,0),nvl(fn_higt_ipchalper(p.ipnum),0)),'FM999,999,999,999') as hprice"
    list_sql += ", fn_basedata_name(3,1,p.status) as status,TO_CHAR(a.indate,'YYYY.MM.DD') as indate "
    list_sql += "from actmain a , actmainde b , ipchal p "
    list_sql += "where b.anum = a.anum and p.anum = a.anum"
    list_sql += ") T ) where r_num between "+sp+" and "+ep

    # palist = pd.read_sql(list_sql,con=conn)
    # alist = palist.to_dict()
    cursor = conn.cursor()
    cursor.execute(list_sql)
    alist = cursor.fetchall()
    cursor.close()
    return render(request, "auction/auction_list.html", {"alist": alist,"asp":sp,"aed":ep,"aorder":orderby,"pcnt":pcnt})

def list_sel_cnt(request):
    conn = ora.connect('semiproject/kosmo@localhost:1521/orcl')
    list_sql_cnt = "select count(a.bid) as cnt from actmain a , actmainde b , ipchal p where b.anum = a.anum and p.anum = a.anum"
    cursor = conn.cursor()
    cursor.execute(list_sql_cnt)
    count = cursor.fetchall()
    print('cnt:', count[0][0])
    conn.close()
    return render(request, "auction/list_count.html", {"count": count[0][0]})

def list_sel_detail(request):
    tnum = request.GET["num"]

    if request.session.get("aid", False):
        bid = request.session["aid"]
    else:
        bid = ""

    print("num:",tnum);
    conn = ora.connect('semiproject/kosmo@localhost:1521/orcl')
    list_sql = "select a.anum,a.bid,fn_yongdo_name(a.byongdo) as yongdo,a.baddra as addr,a.bweight,a.tweight,a.hit,b.wimage,b.imagea,b.imageb,b.imagec"
    list_sql += ",TO_CHAR(p.ideprice,'FM999,999,999,999') as ideprice,p.subject,TO_CHAR(p.enddate,'YYYY-MM-DD HH24:MI:SS') as enddate"
    list_sql += ",TO_CHAR( DECODE(nvl(fn_higt_ipchalper(p.ipnum),0),0,nvl(p.ideprice,0),nvl(fn_higt_ipchalper(p.ipnum),0)),'FM999,999,999,999') as hprice"
    list_sql += ", fn_basedata_name(3,1,p.status) as status,TO_CHAR(a.indate,'YYYY.MM.DD') as indate, DECODE(nvl(fn_higt_ipchalper(p.ipnum),0),0,nvl(p.ideprice,0),nvl(fn_higt_ipchalper(p.ipnum),0)) as inhprice,p.ipnum "
    list_sql += "from actmain a , actmainde b , ipchal p "
    list_sql += "where b.anum = a.anum and p.anum = a.anum "
    list_sql += " and a.anum ="+tnum

    cursor = conn.cursor()
    cursor.execute(list_sql)
    plist = cursor.fetchall()
    cursor.close()
    alist = plist[0];

    logdate = datetime.strptime(alist[13], '%Y-%m-%d %H:%M:%S')
    result = logdate-datetime.now()

    if result.total_seconds() < 0:
        timer = "만료";
    else:
        timer = alist[13];

    return render(request,"auction/auction_list_detail.html",{"alist": alist,"timer":timer,"bid":bid})

@csrf_exempt
def list_ip_ins(request):
    id = request.POST["bid"]
    price = int(request.POST["ipprice"])
    ipnum = int(request.POST["ipnum"])
    print('id:',id,'price:',price,'ipnum',ipnum)
    conn = ora.connect('semiproject/kosmo@localhost:1521/orcl')
    cursor = conn.cursor()
    sql_insert = 'insert into ipchalper values(ipchalper_seq.nextVal,:ipnum,:bid,:ipprice,sysdate,sysdate,null)'
    cursor.execute(sql_insert,ipnum=ipnum,bid=id,ipprice=price)
    cursor.close()
    conn.commit()
    conn.close()
    return redirect("/auction/list")