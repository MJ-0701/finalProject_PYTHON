from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import cx_Oracle as ora
import json

def index(request):
    if request.session.get('aid',False):
        aid = request.session["aid"]
        agubun_s = request.session["agubun_s"]
        conn = ora.connect('semiproject/kosmo@192.168.0.117:1521/orcl')
        list_sql = "select a.aid,b.gon from signup a , chatnow b where b.gaid = a.aid"
        cursor = conn.cursor()
        cursor.execute(list_sql)
        plist = cursor.fetchall()
        cursor.close()
        return render(request, 'chat/index.html', {"aid": aid, "agubun_s": agubun_s, "plist": plist})
    else:
        return redirect("/gologin")



def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })