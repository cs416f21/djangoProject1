from django.urls import path
from . import views # Import the views file  . indicates the current directory as both views.py and this file are in the same directory

urlpatterns = [
    path('<str:my_name>', views.hello), # <str:my_name> allows us to capture values from the url so that your function can use this value dynamically
    path('goodbye/', views.goodbye), # if goodbye is included after the localhost address, maps to goodbye function in the views.py
]