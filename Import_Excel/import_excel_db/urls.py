from django.urls import path
from . import views
urlpatterns =[
path("",views.Import_Excel_pandas,name="Import_Excel_pandas"),
path('Import_Excel_pandas/', views.Import_Excel_pandas,name="Import_Excel_pandas"),
] 