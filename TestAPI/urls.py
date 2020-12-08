from django.urls import path
from TestAPI import views

urlpatterns = [
  path('test-struct/', views.TestStructViewSet.as_view({'get': 'retrieve', 'post': 'create'})),
  path('test-structs/', views.TestStructViewSet.as_view({'get': 'list'})),
  path('pred/', views.pred),
  path('myApp/line', views.app_bar),
  path('myApp/hm', views.app_bar),
  path('inference/step/', views.inference_step),
  path('inference/exercise/', views.inference_exercise),
  path('check/', views.check_status),
  path('start/', views.start),
  path('pred-tail/', views.pred_tail),
]
