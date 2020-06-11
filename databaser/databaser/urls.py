"""databaser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import databaser_website.views as databaser_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tester/', databaser_view.sql_query_sqlite),
    path('person_select/',databaser_view.person_select),
    path('person_insert/',databaser_view.person_insert),
    path('person_delete/',databaser_view.person_delete),
    path('select_all_person/',databaser_view.select_all_person),
    path('select_all_location/',databaser_view.select_all_location),
    path('select_all_doctor/',databaser_view.select_all_doctor),
    path('sum_measurement_one_year_for_people/',databaser_view.sum_measurement_one_year_for_people),
    path('person_update_doctor/',databaser_view.person_update_doctor),
    path('sql_query_sqlite_select/',databaser_view.sql_query_sqlite_select),
    path('check_free_doctor_by_not_exist/',databaser_view.check_free_doctor_by_not_exist),
    path('check_busy_doctor_by_exist/',databaser_view.check_busy_doctor_by_exist),
    path('check_person_location_by_in/', databaser_view.check_person_location_by_in),
    path('check_person_location_by_notin/', databaser_view.check_person_location_by_notin),
    path('having_all_average_weight_over_85/', databaser_view.having_all_average_weight_over_85),
    path('count_uniquc_condition/', databaser_view.count_uniquc_condition),
    path('avg_measurement_temp_for_people/', databaser_view.avg_measurement_temp_for_people),
    path('max_measurement_pressure_for_people/', databaser_view.max_measurement_pressure_for_people),
    path('min_measurement_pressure_for_people/', databaser_view.min_measurement_pressure_for_people),
    path('sum_measurement_one_year_for_people/',databaser_view.sum_measurement_one_year_for_people),
    path('qwe/',databaser_view.qwe),
    path('qwe2/',databaser_view.qwe2)
]
