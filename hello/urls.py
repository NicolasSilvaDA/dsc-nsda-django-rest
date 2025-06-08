from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
    path('param/', views.hello_world_param),
    path('path/<str:nome>/<str:sobrenome>/', views.hello_world_path),
    path('path/<str:nome>/<str:sobrenome>/<str:valor>/', views.hello_world_path_valor),
    path('usuario/', views.hello_world_usuario),
    path('testejson/', views.hello_world_json),
]
