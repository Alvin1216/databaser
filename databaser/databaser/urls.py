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
    path('person_update_doctor/',databaser_view.person_update_doctor),
    path('qwe/',databaser_view.qwe),
]
