from django.shortcuts import render
from databaser_website.models import Condition
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sqlite3
import sys
import traceback

conn = sqlite3.connect('/Users/alvinhuang/Desktop/covid_database/covid_data.db',check_same_thread = False)
conn.execute("PRAGMA foreign_keys = ON")
conn.commit()


@csrf_exempt
def sql_query_sqlite(request):
    if request.method == "POST":
        qse = str(request.POST['query_string'])
        print(qse)
        try:
            cursor = conn.execute(qse)
            names = list(map(lambda x: x[0], cursor.description))
            print(names)
            for row in cursor:
                print(row)
            return JsonResponse({"status": "200"})
        except:
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})
@csrf_exempt
def person_select(request):
    if request.method == "POST":
        person_id = str(request.POST['person_id'])
        qse = "SELECT * FROM person WHERE person_id = " + person_id
        print(qse)
        try:
            cursor = conn.execute(qse)
            names = list(map(lambda x: x[0], cursor.description))
            print(names)
            for row in cursor:
                print(row)
            return JsonResponse({"status": "200"})
        except:
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def person_insert(request):
    if request.method == "POST":
        gender = str(request.POST['gender'])
        race = str(request.POST['race'])
        age = request.POST['age']
        name = request.POST['name']
        location_id = request.POST['location_id']
        doctor_id = request.POST['doctor_id']
        birth_datetime = str(request.POST['birth_datetime'])

        #get max id
        max_id_qse = "SELECT MAX(person_id) FROM person"
        cursor = conn.execute(max_id_qse)
        data = cursor.fetchall()
        person_id = int(data[0][0]) + 1

        insert_qse = "INSERT INTO person VALUES (%s,\"%s\",\"%s\",\"%s\",\"%s\",%s, %s, %s)" % (int(person_id),str(name),str(birth_datetime),str(gender),str(race),int(age),int(location_id),int(doctor_id))
        print(insert_qse)
        try:
            conn.execute(insert_qse)
            conn.commit()
            print("success!")
            return JsonResponse({"status": "200"})
        except Exception as e:
            get_error(e)
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})


@csrf_exempt
def person_delete(request):
    if request.method == "POST":
        person_id = int(request.POST['person_id'])

        delete_qse = "DELETE FROM person WHERE person_id = {id}".format(id=person_id)
        #insert_qse = "INSERT INTO person VALUES (%s,\"%s\",\"%s\",\"%s\",\"%s\",%s, %s, %s)" % (int(person_id),str(name),str(birth_datetime),str(gender),str(race),int(age),int(location_id),int(doctor_id))
        print(delete_qse)
        try:
            conn.execute(delete_qse)
            conn.commit()
            print("success!")
            return JsonResponse({"status": "200"})
        except Exception as e:
            get_error(e)
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})


@csrf_exempt
def person_update_doctor(request):
    # TODO : update custom columns and table
    if request.method == "POST":
        person_id = int(request.POST['person_id'])
        doctor_id = int(request.POST['doctor_id'])
        update_qse = "UPDATE person SET doctor_id = {doctor_id} WHERE person_id = {id}".format(doctor_id=doctor_id,id=person_id)
        print(update_qse)
        try:
            conn.execute(update_qse)
            conn.commit()
            print("success!")
            return JsonResponse({"status": "200"})
        except Exception as e:
            get_error(e)
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})


def get_error(e):
    error_class = e.__class__.__name__  # 取得錯誤類型
    detail = e.args[0]  # 取得詳細內容
    cl, exc, tb = sys.exc_info()  # 取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1]  # 取得Call Stack的最後一筆資料
    fileName = lastCallStack[0]  # 取得發生的檔案名稱
    lineNum = lastCallStack[1]  # 取得發生的行號
    funcName = lastCallStack[2]  # 取得發生的函數名稱
    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
    print(errMsg)

def qwe(request):
    return render(request, "databaser_website/base.html", locals())