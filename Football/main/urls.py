from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('mode/',views.theme_mode_view,name='theme_mode_view')
]
