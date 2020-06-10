from django.shortcuts import render
from databaser_website.models import Condition
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sqlite3,json
import sys
import traceback

conn = sqlite3.connect('/Users/alvinhuang/Desktop/covid_database/covid_data.db',check_same_thread = False)
conn.execute("PRAGMA foreign_keys = ON")
conn.commit()


@csrf_exempt
def sql_query_sqlite(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)
        qse = str(json_data['query_string'])
        print(qse)
        try:
            conn.execute(qse)
            conn.commit()
            print("success!")
            return JsonResponse({"status": "200"})
        except:
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

def sql_query_sqlite_select(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)
        qse = str(json_data['query_string'])
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
        json_data = json.loads(request.body)
        print(json_data)
        person_id = str(json_data['person_id'])
        qse = "SELECT * FROM person WHERE person.person_id = " + person_id
        print(qse)
        try:
            return_data = {}
            cursor = conn.execute(qse)
            names = list(map(lambda x: x[0], cursor.description))
            print(names)
            return_data['col'] = names
            row_data = []
            for row in cursor:
                print(list(row))
                row_data.append(list(row))
            return_data['data'] = row_data
            return JsonResponse(return_data)
        except:
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def select_all_location(request):
    if request.method == "POST":
        qse = "SELECT * FROM location"
        print(qse)
        try:
            return_data = {}
            cursor = conn.execute(qse)
            names = list(map(lambda x: x[0], cursor.description))
            print(names)
            return_data['col'] = names
            row_data = []
            for row in cursor:
                print(list(row))
                row_data.append(list(row))
            return_data['data'] = row_data
            return JsonResponse(return_data)
        except:
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def select_all_doctor(request):
    if request.method == "POST":
        qse = "SELECT * FROM doctor"
        print(qse)
        try:
            return_data = {}
            cursor = conn.execute(qse)
            names = list(map(lambda x: x[0], cursor.description))
            print(names)
            return_data['col'] = names
            row_data = []
            for row in cursor:
                print(list(row))
                row_data.append(list(row))
            return_data['data'] = row_data
            return JsonResponse(return_data)
        except:
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def select_all_person(request):
    if request.method == "POST":
        qse = "SELECT * FROM person"
        print(qse)
        try:
            return_data = {}
            cursor = conn.execute(qse)
            names = list(map(lambda x: x[0], cursor.description))
            print(names)
            return_data['col'] = names
            row_data = []
            for row in cursor:
                print(list(row))
                row_data.append(list(row))
            return_data['data'] = row_data
            return JsonResponse(return_data)
        except:
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def person_insert(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)
        gender = str(json_data['gender'])
        race = str(json_data['race'])
        age = json_data['age']
        name = json_data['name']
        location_id = json_data['location_id']
        doctor_id = json_data['doctor_id']
        birth_datetime = str(json_data['birth_datetime'])

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
        json_data = json.loads(request.body)
        print(json_data)
        person_id = int(json_data['person_id'])
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
    print(request.method)
    if request.method == "POST":
        json_data = json.loads(request.body)
        person_id = json_data['person_id']
        doctor_id = json_data['doctor_id']
        print(json_data)
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

@csrf_exempt
def check_free_doctor_by_not_exist(request):
    # TODO : update custom columns and table
    if request.method == "POST":
        json_data = json.loads(request.body)
        #person_id = int(json_data['person_id'])
        #doctor_id = int(json_data['doctor_id'])
        update_qse = "SELECT * FROM doctor WHERE NOT EXISTS (SELECT * FROM person WHERE person.doctor_id = doctor.doctor_id)"
        print(update_qse)
        try:

            cursor = conn.execute(update_qse)
            names = list(map(lambda x: x[0], cursor.description))

            return_data = {}
            print(names)
            return_data['col'] = names
            row_data = []
            for row in cursor:
                print(list(row))
                row_data.append(list(row))
            return_data['data'] = row_data
            for row in cursor:
                print(row)

            print("success!")
            return JsonResponse(return_data)
        except Exception as e:
            get_error(e)
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def check_busy_doctor_by_exist(request):
    # TODO : update custom columns and table
    if request.method == "POST":
        json_data = json.loads(request.body)
        #person_id = int(request.POST['person_id'])
        #doctor_id = int(request.POST['doctor_id'])
        update_qse = "SELECT * FROM doctor WHERE EXISTS (SELECT * FROM person WHERE person.doctor_id = doctor.doctor_id)"
        print(update_qse)
        try:
            cursor = conn.execute(update_qse)
            names = list(map(lambda x: x[0], cursor.description))
            return_data = {}
            print(names)
            return_data['col'] = names
            row_data = []
            for row in cursor:
                print(list(row))
                row_data.append(list(row))
            return_data['data'] = row_data
            for row in cursor:
                print(row)
            print("success!")
            return JsonResponse(return_data)
        except Exception as e:
            get_error(e)
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def check_person_location_by_in(request):
    # TODO : update custom columns and table
    if request.method == "POST":
        json_data = json.loads(request.body)
        #loc_1 = int(request.POST['location_1'])
        #loc_2 = int(request.POST['location_2'])
        #update_qse = "SELECT * FROM person WHERE location_id IN ({loc_1},{loc_2})".format(loc_1=loc_1,loc_2=loc_2)
        update_qse = "SELECT * FROM person WHERE location_id IN (30,65)"
        print(update_qse)
        try:
            cursor = conn.execute(update_qse)
            names = list(map(lambda x: x[0], cursor.description))
            return_data = {}
            print(names)
            return_data['col'] = names
            row_data = []
            for row in cursor:
                print(list(row))
                row_data.append(list(row))
            return_data['data'] = row_data
            for row in cursor:
                print(row)
            print("success!")
            return JsonResponse(return_data)
        except Exception as e:
            get_error(e)
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def check_person_location_by_notin(request):
    # TODO : update custom columns and table
    if request.method == "POST":
        #loc_1 = int(request.POST['location_1'])
        #loc_2 = int(request.POST['location_2'])
        #update_qse = "SELECT * FROM person WHERE location_id IN ({loc_1},{loc_2})".format(loc_1=loc_1,loc_2=loc_2)
        update_qse = "SELECT * FROM person WHERE location_id NOT IN (30,65)"
        print(update_qse)
        try:
            cursor = conn.execute(update_qse)
            names = list(map(lambda x: x[0], cursor.description))
            return_data = {}
            print(names)
            return_data['col'] = names
            row_data = []
            for row in cursor:
                print(list(row))
                row_data.append(list(row))
            return_data['data'] = row_data
            for row in cursor:
                print(row)
            print("success!")
            return JsonResponse(return_data)
        except Exception as e:
            get_error(e)
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def having_all_average_weight_over_85(request):
    if request.method == "POST":
        update_qse = "SELECT person_id,AVG(value_as_number) FROM new_measurement WHERE measurement_name = \"Body weight\" GROUP BY person_id HAVING AVG(value_as_number)>85"
        print(update_qse)
        try:
            cursor = conn.execute(update_qse)
            names = list(map(lambda x: x[0], cursor.description))
            return_data = {}
            print(names)
            return_data['col'] = names
            row_data = []
            for row in cursor:
                print(list(row))
                row_data.append(list(row))
            return_data['data'] = row_data
            for row in cursor:
                print(row)
            print("success!")
            return JsonResponse(return_data)
        except Exception as e:
            get_error(e)
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def count_uniquc_condition(request):
    if request.method == "POST":
        person_id = request.POST['person_id']
        update_qse =  "SELECT COUNT (DISTINCT condition_occurrence_id) FROM condition_person WHERE person_id = {person_id}".format(person_id=person_id)
        print(update_qse)
        try:
            cursor = conn.execute(update_qse)
            names = list(map(lambda x: x[0], cursor.description))
            return_data = {}
            print(names)
            return_data['col'] = names
            row_data = []
            for row in cursor:
                print(list(row))
                row_data.append(list(row))
            return_data['data'] = row_data
            for row in cursor:
                print(row)
            print("success!")
            return JsonResponse(return_data)
        except Exception as e:
            get_error(e)
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def avg_measurement_temp_for_people(request):
    if request.method == "POST":
        person_id = request.POST['person_id']
        update_qse =  "SELECT person_id,ROUND(AVG(value_as_number),1) FROM new_measurement WHERE measurement_name = \"Body temperature\" GROUP BY person_id"
        print(update_qse)
        try:
            cursor = conn.execute(update_qse)
            for row in cursor:
                print(row)
            print("success!")
            return JsonResponse({"status": "200"})
        except Exception as e:
            get_error(e)
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def max_measurement_pressure_for_people(request):
    if request.method == "POST":
        person_id = request.POST['person_id']
        update_qse =  "SELECT person_id,ROUND(MAX(value_as_number),1) FROM new_measurement WHERE measurement_name = \"Diastolic blood pressure\" GROUP BY person_id"
        print(update_qse)
        try:
            cursor = conn.execute(update_qse)
            for row in cursor:
                print(row)
            print("success!")
            return JsonResponse({"status": "200"})
        except Exception as e:
            get_error(e)
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def min_measurement_pressure_for_people(request):
    if request.method == "POST":
        person_id = request.POST['person_id']
        update_qse =  "SELECT person_id,ROUND(MIN(value_as_number),1) FROM new_measurement WHERE measurement_name = \"Diastolic blood pressure\" GROUP BY person_id"
        print(update_qse)
        try:
            cursor = conn.execute(update_qse)
            for row in cursor:
                print(row)
            print("success!")
            return JsonResponse({"status": "200"})
        except Exception as e:
            get_error(e)
            return JsonResponse({"status": "SQL wrong~"})
    else:
        return JsonResponse({"status": "205"})

@csrf_exempt
def sum_measurement_one_year_for_people(request):
    if request.method == "POST":
        year = request.POST['year']
        update_qse =  "SELECT SUM(numofyear) FROM (SELECT person_id,count(measurement_id) AS numofyear FROM new_measurement" \
                      " WHERE measurement_date>=\"{year}-01-01\" AND measurement_date<=\"{year}-12-31\" GROUP BY person_id)".format(year=year)
        print(update_qse)
        try:
            cursor = conn.execute(update_qse)
            for row in cursor:
                print(row)
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

def basic_render(request):
    if request.method == "POST":
        type = request.POST['type']
        if type == "person_select":
            data = person_select(request)
        elif type == "person_insert":
            data = person_insert(request)
        elif type == "person_delete":
            data = person_delete(request)
        elif type =="person_update_doctor":
            data = person_update_doctor(request)
        else:
            data = "something_wrong"
    else:
        return JsonResponse({"status": "205"})

def qwe(request):
    return render(request, "databaser_website/base.html", locals())

def qwe2(request):
    return render(request, "databaser_website/base2.html", locals())