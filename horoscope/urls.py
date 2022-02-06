from django.urls import path

from horoscope import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('type/', views.type),
    path('type/<str:type_zodiac>/', views.get_info_about_type_zodiac, name='horoscope-type'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name = 'horoscope-name'),
    path('<int:month>/<int:day>/', views.get_info_by_date),

]